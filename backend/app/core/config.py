import os


class Settings:

    APP_NAME = "Alpha Radar"

    OPENAI_KEY = os.getenv(
        "OPENAI_API_KEY"
    )


settings = Settings()