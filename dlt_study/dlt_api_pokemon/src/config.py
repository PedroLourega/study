from pathlib import Path
import tomllib
import os
import urllib3
from dlt.sources.helpers.requests import Session as DltSession
from dotenv import load_dotenv

BASEDIR = Path(__file__).resolve().parent.parent


def load_config() -> dict:
    env_path = BASEDIR / ".env"

    if not env_path.exists():
        raise FileNotFoundError(f"ARQUIVO .ENV NÃO ENCONTRADO EM: f{env_path}")

    load_dotenv(env_path)
    if not os.getenv("DESTINATION__POSTGRES__CREDENTIALS"):
        raise ValueError

    settings_path = BASEDIR / "settings.toml"
    with open(settings_path, "rb") as file:
        return tomllib.load(file)


def ssl_config(verif_ssl):
    if verif_ssl is True:
        return
    if verif_ssl is False:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    original_send = DltSession.send

    def __custom_send(self, request, **kwargs):
        kwargs.setdefault("verify", verif_ssl)
        return original_send(self, request, **kwargs)

    DltSession.send = __custom_send
