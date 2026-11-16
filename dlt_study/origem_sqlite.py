import dlt
import pandas as pd
import os


PATH_EXCEL = os.path.join("content", "streamings_rate.xlsx")


# LÊ A PLANILHA EXCEL
@dlt.resource(
    table_name="series",
    write_disposition="merge",
    primary_key="serie",
)
def extract_excel(path_excel):
    df = pd.read_excel(path_excel, sheet_name="series")

    # CONVERTE DF EM DICT
    yield df.to_dict(orient="records")


# CONFIG SQLITE
def load_sqlite():
    pipeline = dlt.pipeline(
        pipeline_name="excel_sqlite",
        destination="sqlalchemy",
        dataset_name="catalogo_series",
    )

    # EXECUTA O PIPILINE DE CARGA
    info = pipeline.run(extract_excel(PATH_EXCEL))
    print("CARGA SQLITE COMPLETA!!!")
    print(info)


if __name__ == "__main__":
    load_sqlite()
