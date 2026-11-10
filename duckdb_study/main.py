# IMPORTS
import os
import duckdb
from dotenv import load_dotenv

# CARREGAR DADOS DOTENV

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

DB_URI = f"dbname={db_host} user={db_user} password={db_pass} host={db_name}"


def get_duckdb_con():
    "FUNÇÃO QUE GERA A CONEXÃO DO DUCKDB"
    con = duckdb.connect(":memory:")

    # ':memory:' permite centralizar o processo executado em memória
    con.execute("PRAGMA enable_progress_bar=true;")

    # 'threads=4' permite limitar o uso de threads
    con.execute("PRAGMA threads=4;")

    # instalação e carregamento de extensões
    con.execute("INSTALL postgres;")
    con.execute("LOAD postgres")

    return con


# FUNÇÕES DO PIPELINE
def main(con): ...


if __name__ == "__main__":
    main()
