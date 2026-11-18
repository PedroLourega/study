import pipeline
import origem_sqlite


def main():
    print("INICIANDO PROCESSAMENTO...\nCOPIANDO DE EXCEL -> SQLITE")
    origem_sqlite.load_sqlite()

    print("PROXIMA ETAPA INICIADA...\nSQLITE -> POSTGRESQL...")
    pipeline.sqlite_postgres()

    print("FLUXO DO PIPELINE FINALIZADO!")


if __name__ == "__main__":
    main()
