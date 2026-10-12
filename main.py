import argparse
import os
import subprocess

import yaml
from dotenv import load_dotenv

from settings import Settings


def export_envs(environment: str = "dev") -> None:
    load_dotenv(f"config/.env.{environment}", override=True)


def export_secrets(secrets_path: str = "secrets.yaml") -> None:
    decrypted = subprocess.run(
        ["sops", "--decrypt", secrets_path], capture_output=True, text=True, check=True
    ).stdout
    for key, value in yaml.safe_load(decrypted).items():
        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified .env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
