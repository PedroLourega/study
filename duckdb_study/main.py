# IMPORTS
from logging import config
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

# COLUNA DE ID
COL_ID = "objectid"

# CARREGAR DADOS DOTENV

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

DB_URI = f"dbname={db_host} user={db_user} password={db_pass} host={db_name}"

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
    FUNÇÃO QUE GERA A CONEXÃO DO DUCKDB
    """
    # dicionário de configuração
    config_dict = {
        "threads": "4",
        "memory_limit": "4GB",
    }
    # gerador de conexão':memory:' permite centralizar o processo executado em memória
    con = duckdb.connect(":memory:", config=config_dict)
    # adiciona uma barra de progresso
    # con.execute("SET enable_progress_bar=false;")

    # instalação e carregamento de extensões
    con.execute("INSTALL postgres;")
    con.execute("LOAD postgres;")

    con.execute("INSTALL spatial;")
    con.execute("LOAD spatial;")

    return con


def _get_contagem_ids(con: duckdb.DuckDBPyConnection, src_schema, src_nome_tabela):

    limite = con.execute(f"""
    SELECT MIN({COL_ID}), MAX({COL_ID}) FROM db_source.{src_schema}.{src_nome_tabela}
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

    # CONECTA O DUCKDB COM O BANCO ORIGEM (READ ONLY)
    con.execute(f"ATTACH '{SOURCE_DB_URI}' AS db_source (TYPE postgres, READ_ONLY);")

    # CONECTA O DUCKDB COM O BANCO DE DESTINO
    con.execute(f"ATTACH '{TARGET_DB_URI}' AS db_target (TYPE postgres);")

    min_id, max_id = _get_contagem_ids(con, src_schema, src_nome_tabela)

    total_lotes = ((max_id - min_id) // TAMANHO_LOTE) + 1

    print(
        f"BANCOS CONECTADOS COM SUCESSO!!! \nINICIANDO PROCESSO DE CÓPIA DOS DADOS...\nSCHEMA_ORIGEM:'{src_schema}'\nSCHEMA_DESTINO:'{trg_schema}'\nNOME_TABELA_ORIGEM:'{src_nome_tabela}'\nNOME_TABELA_DESTINO:'{trg_nome_tabela}'"
    )

    # QUERY PARA CRIAR A TABELA SE ELA JA NAO EXISTIR
    query_create_table = f"""
    CREATE TABLE IF NOT EXISTS db_target.{trg_schema}.{trg_nome_tabela} AS
    SELECT * FROM db_source.{src_schema}.{src_nome_tabela} LIMIT 0;
    """

    # QUERY DE VERIFICAÇÃO
    tabela_existe = con.execute(
        f"""
    SELECT EXISTS (
        SELECT 1
        FROM db_target.information_schema.tables
        WHERE table_schema = '{trg_schema}' AND table_name = '{trg_nome_tabela}' 
        );
    """
    ).fetchone()[0]

    # QUERY PARA COPIAR A TABELA DE UM BANCO PARA OUTRO
    query_copy = f"""
    INSERT INTO db_target.{trg_schema}.{trg_nome_tabela}
    SELECT * FROM db_source.{src_schema}.{src_nome_tabela};
    """

    try:
        if tabela_existe:
            print(
                f'NÃO FOI NECESSÁRIO CRIAR A TABELA POIS ELA JÁ ESTÁ PRESENTE NO BANCO DE DADOS: "{trg_schema}"."{trg_nome_tabela}"'
            )
            # con.execute(query_copy)
            # print("SUCESSO AO EXECUTAR A INSERÇÃO DOS DADOS!!!")
        else:
            con.execute(query_create_table)
            # con.execute(query_copy)
            print(
                f"TABELA NÃO FOI ENCONTRADA.\nCRIADA EM: '{trg_schema}'.'{trg_nome_tabela}' CRIADA COM SUCESSO"
            )
            # print("SUCESSO AO EXECUTAR A INSERÇÃO DOS DADOS!!!")

        with tqdm(total=total_lotes, desc="Controle de Progresso", unit="lote") as pbar:
            id_atual = min_id

            while id_atual <= max_id:
                limite_sup = id_atual + TAMANHO_LOTE - 1

                query_lote = f"""
                INSERT INTO db_target.{trg_schema}.{trg_nome_tabela}
                SELECT * FROM db_source.{src_schema}.{src_nome_tabela}
                WHERE {COL_ID} BETWEEN {id_atual} AND {limite_sup};
                """
            con.execute(query_lote)
            print(
                f"DADOS FORAM INSERIDOS COM SUCESSO!!\nSCHEMA.TABLE_NAME:{trg_schema}.{trg_nome_tabela}"
            )

            id_atual += TAMANHO_LOTE
            pbar.update(1)
    except Exception as e:
        print(f"ERRO AO EXECUTAR A QUERY...\nERRO:{e}")
    finally:
        con.close()


# FUNÇÕES DO PIPELINE
def main():
    copiar_tabela_duckdb(
        _get_duckdb_con(), src_schema, trg_schema, src_nome_tabela, trg_nome_tabela
    )


if __name__ == "__main__":
    main()
