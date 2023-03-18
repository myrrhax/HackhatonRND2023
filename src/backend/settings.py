from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    port: SecretStr
    app_host: SecretStr
    postgres_db: SecretStr
    postgres_user: SecretStr
    host: SecretStr
    postgres_password: SecretStr
    jwt_secret: SecretStr
    algorithm: SecretStr

    class Config:
        env_file: str = '.env'
        env_file_encoding: str = 'utf-8'

config = Settings()