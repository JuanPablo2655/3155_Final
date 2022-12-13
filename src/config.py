import os

from dotenv import load_dotenv

load_dotenv()

isCI = os.getenv("CI") == "true"


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


postgres_uri = os.getenv(
    'POSTGRES_URI') if isCI else validate_env("POSTGRES_URI")
bcrypt_rounds = os.getenv(
    'BCRYPT_ROUNDS') if isCI else validate_int_env("BCRYPT_ROUNDS")
secret_key = os.getenv('SECRET_KEY') if isCI else validate_env("SECRET_KEY")
