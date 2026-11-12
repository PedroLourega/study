# IMPORTS
import os
import duckdb
from tqdm import tqdm
from dotenv import load_dotenv

# CONFIGURAÇÕES DE BANCO
src_schema, trg_schema, src_nome_tabela, trg_nome_tabela = (
    "public",
    "public",
    "car_imoveis_validos_a",
    "car_imoveis_validos_a",
)

# VARIAVEL GLOBAL PARA ARMAZENAR O VALOR DO LOTE
TAMANHO_LOTE = 100000

# VARIAVEL GLOBAL QUE ARMAZENA A COLUNA DE ID
COL_ID = "objectid"

# CARREGAR DADOS DOTENV
load_dotenv()

# SOURCE
src_db_host = os.getenv("SOURCE_DB_HOST")
src_db_user = os.getenv("SOURCE_DB_USER")
src_db_pass = os.getenv("SOURCE_DB_PASS")
src_db_name = os.getenv("SOURCE_DB_NAME")
src_db_port = os.getenv("SOURCE_DB_PORT")

SOURCE_DB_URI = f"dbname={src_db_name} password={src_db_pass} user={src_db_user} host={src_db_host} port={src_db_port}"

# TARGET
trg_db_host = os.getenv("TARGET_DB_HOST")
trg_db_user = os.getenv("TARGET_DB_USER")
trg_db_pass = os.getenv("TARGET_DB_PASS")
trg_db_name = os.getenv("TARGET_DB_NAME")
trg_db_port = os.getenv("TARGET_DB_PORT")

TARGET_DB_URI = f"dbname={trg_db_name} password={trg_db_pass} user={trg_db_user} host={trg_db_host} port={trg_db_port}"


def _get_duckdb_con():
    """
    FUNÇÃO QUE GERA A CONEXÃO DO DUCKDB E CONFIGURA A FERRAMENTA
    """
    config_dict = {
        "threads": "4",
        "memory_limit": "4GB",
    }
    con = duckdb.connect(":memory:", config=config_dict)

    con.execute("INSTALL postgres;")
    con.execute("LOAD postgres;")

    con.execute("INSTALL spatial;")
    con.execute("LOAD spatial;")

    return con


def _get_contagem_ids(con: duckdb.DuckDBPyConnection, src_schema, src_nome_tabela):
    limite = con.execute(f"""
        SELECT MIN({COL_ID}), MAX({COL_ID}) 
        FROM db_source.{src_schema}.{src_nome_tabela}
    """).fetchone()

    return limite[0], limite[1]


def copiar_tabela_duckdb(
    con: duckdb.DuckDBPyConnection,
    src_schema,
    trg_schema,
    src_nome_tabela,
    trg_nome_tabela,
):
    """
    FUNÇÃO PARA COPIAR UMA TABELA DE UM BANCO PARA OUTRO
    """
    try:
        # CONECTA O DUCKDB COM O BANCO ORIGEM (READ ONLY)
        con.execute(
            f"ATTACH '{SOURCE_DB_URI}' AS db_source (TYPE postgres, READ_ONLY);"
        )

        # CONECTA O DUCKDB COM O BANCO DE DESTINO
        con.execute(f"ATTACH '{TARGET_DB_URI}' AS db_target (TYPE postgres);")

        print(
            f"BANCOS CONECTADOS COM SUCESSO!!! \nINICIANDO PROCESSO DE CÓPIA DOS DADOS...\n"
            f"ORIGEM - SCHEMA.NOME_TABELA:'{src_schema}'.'{src_nome_tabela}'\nDESTINO - SCHEMA.NOME_TABELA:'{trg_schema}'.'{trg_nome_tabela}'"
        )

        # QUERY PARA CRIAR A TABELA SE ELA JA NAO EXISTIR
        query_create_table = f"""
            CREATE TABLE IF NOT EXISTS db_target.{trg_schema}.{trg_nome_tabela} AS
            SELECT * FROM db_source.{src_schema}.{src_nome_tabela} LIMIT 0;
        """

        # QUERY DE VERIFICAÇÃO PARA A COLETA DOS CAMPOS PRESENTES NA TABELA
        tabela_existe = con.execute(f"""
            SELECT EXISTS (
                SELECT 1
                FROM db_target.information_schema.tables
                WHERE table_schema = '{trg_schema}' AND table_name = '{trg_nome_tabela}' 
            );
        """).fetchone()[0]

        # CONDIÇÃO SE A TABELA EXISTE OU NÃO
        if tabela_existe:
            print(
                f'NÃO FOI NECESSÁRIO A CRIAÇÃO DA TABELA POIS ELA JÁ ESTÁ PRESENTE NO BANCO DE DADOS: "{trg_schema}"."{trg_nome_tabela}"'
            )
        else:
            con.execute(query_create_table)
            print(
                f"TABELA NÃO FOI ENCONTRADA NO BANCO...\nCRIADA EM: '{trg_schema}'.'{trg_nome_tabela}' COM SUCESSO!!"
            )

        # DEFININDO VALOR DO ID MIN E MAX ATRAVÉS DA FUNÇÃO DE COLETA DE IDS
        min_id, max_id = _get_contagem_ids(con, src_schema, src_nome_tabela)

        # CALCULA O TOTAL DE LOTES
        total_lotes = ((max_id - min_id) // TAMANHO_LOTE) + 1

        # CONFIGURAÇÃO DA BARRA DE PROGRESSO
        with tqdm(total=total_lotes, desc="Controle de Progresso", unit="lote") as pbar:
            id_atual = min_id

            # LOOP PARA SOMAR OS IDs
            while id_atual <= max_id:
                limite_sup = id_atual + TAMANHO_LOTE - 1

                # QUERY PARA INSERIR DADOS APENAS QUE ESTÃO ENTRE OS IDs SELECIONADOS DO LOTE
                query_lote = f"""
                    INSERT INTO db_target.{trg_schema}.{trg_nome_tabela}
                    SELECT * FROM db_source.{src_schema}.{src_nome_tabela}
                    WHERE {COL_ID} BETWEEN {id_atual} AND {limite_sup};
                """
                con.execute(query_lote)

                # ATUALIZA A BARRA DE PROGRESSO COM O VALOR DO LOTE ATUAL
                id_atual += TAMANHO_LOTE
                pbar.update(1)

        print(
            f"\nDADOS FORAM INSERIDOS COM SUCESSO, PROCESSO FINALIZADO✅!!\nSCHEMA.TABLE_NAME:{trg_schema}.{trg_nome_tabela}"
        )

    except Exception as e:
        print(f"\nERRO AO EXECUTAR A QUERY...\nERRO:{e}")
    # FINALIZA A TRANSAÇÃO
    finally:
        con.close()


# FUNÇÕES DO PIPELINE
def main():
    copiar_tabela_duckdb(
        _get_duckdb_con(), src_schema, trg_schema, src_nome_tabela, trg_nome_tabela
    )


if __name__ == "__main__":
    main()
