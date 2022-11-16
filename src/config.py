import os

from dotenv import load_dotenv

load_dotenv()


def validate_env(_env):
    env = os.getenv(_env)
    if env is None:
        raise ValueError(f"{_env} is not set")
    return env


postgres_uri = validate_env("POSTGRES_URI")
