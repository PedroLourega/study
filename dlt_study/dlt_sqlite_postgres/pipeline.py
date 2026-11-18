import dlt


def ler_sqlite_staging():
    p_sqlite = dlt.attach(pipeline_name="excel_sqlite")
    with p_sqlite.sql_client() as client:
        with client.execute_query("SELECT * FROM series") as cursor:
            colunas = list(cursor.keys())
            return [
                {
                    k: v
                    for k, v in dict(zip(colunas, linha)).items()
                    if not k.startswith("_dlt_")
                }
                for linha in cursor.fetchall()
            ]


@dlt.resource(
    table_name="series",
    write_disposition="merge",
    primary_key="serie",
)
def recurso_series(registros):
    yield registros


def sqlite_postgres():
    registros = ler_sqlite_staging()

    pipeline = dlt.pipeline(
        pipeline_name="mig_sqlite_postgres",
        destination="postgres",
        dataset_name="catalogo_series",
    )

    info = pipeline.run(recurso_series(registros))
    print("CARGA POSTGRES COMPLETA!!!")
    print(info)


if __name__ == "__main__":
    sqlite_postgres()
