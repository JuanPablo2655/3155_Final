import os

from dotenv import load_dotenv

load_dotenv()


def validate_env(_env):
    env = os.getenv(_env)
    if env is None:
        raise ValueError(f"{_env} is not set")
    return env


def validate_int_env(_env):
    env = os.getenv(_env)
    if env is None:
        raise ValueError(f"{_env} is not set")
    try:
        return int(env)
    except ValueError:
        raise ValueError(f"{_env} is not an integer")


postgres_uri = validate_env("POSTGRES_URI")
bcrypt_rounds = validate_int_env("BCRYPT_ROUNDS")
secret_key = validate_env("SECRET_KEY")
