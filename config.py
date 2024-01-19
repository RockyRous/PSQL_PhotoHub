from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = '5432'
    DB_USER: str = 'Alchemy'
    DB_PASS: str = 'Alchemy'
    DB_NAME: str = 'postgres'

    @property
    def DATABASE_URL_psycopg(self):
        """ PostgreSQL + psycopg """
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


if __name__ == "__main__":
    print(settings.DATABASE_URL_psycopg)