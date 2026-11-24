from dlt import dataset
import urllib3
import os
import dlt
import sys
from src.config import load_config, ssl_config
from src.sources.pokeapi import get_pokeapi_source
from src.sources.github import get_github_source


def _run_pokeapi() -> None:
    print("OPÇÃO: [1] SELECIONADA.\nPOKEAPI SELECIONADA")
    settings = load_config()
    pipe_config = settings["pipeline"]
    api_config = settings["pokeapi"]

    ssl_config(api_config.get("verify_ssl", True))

    source = get_pokeapi_source(api_config)
    postgres_destination = dlt.destinations.postgres(
        credentials=os.getenv("DESTINATION__POSTGRES__CREDENTIALS")
    )

    pipeline = dlt.pipeline(
        pipeline_name=pipe_config["name"],
        destination=postgres_destination,
        dataset_name=api_config["dataset_name"],
    )

    print("INICIANDO INGESTÃO DOS DADOS VIA API...")
    load_info = pipeline.run(source)
    print(load_info)
    sys.exit()


def _run_github_api() -> None:
    settings = load_config()
    pipeline_config = settings["pipeline"]
    api_config = settings["github"]

    ssl_config(api_config.get("verify_ssl", True))
    source = get_github_source(api_config)

    postgres_destination = dlt.destinations.postgres(
        credentials=os.getenv("DESTINATION__POSTGRES__CREDENTIALS")
    )

    pipeline = dlt.pipeline(
        pipeline_name=pipeline_config["name"],
        destination=postgres_destination,
        dataset_name=api_config["dataset_name"],
    )

    print("INICIANDO INGESTÃO DOS DADOS VIA API...")
    load_info = pipeline.run(source)
    print(load_info)
    sys.exit()


def run():
    while True:
        response = input("MENU DE SELECAO APIS\n[1]POKEAPI\n[2]GITHUB\n[X]SAIR\n")
        if response == "1":
            _run_pokeapi()
        elif response == "2":
            _run_github_api()
        elif response == "X" or response == "x":
            print("OPÇÃO:[X] SELECIONADA\nFINALIZANDO O PROGRAMA...")
            sys.exit()
        else:
            print("O VALOR DIGITADO É INVÁLIDO...\nTENTE NOVAMENTE")


def main():
    run()


if __name__ == "__main__":
    main()
