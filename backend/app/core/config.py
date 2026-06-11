import os


class Settings:

    APP_NAME = "Alpha Radar"

    OPENAI_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

ROLES = [

    "USER",

    "ADMIN",

    "ANALYST",

    "ENTERPRISE"
]
PLANS = [

    "FREE",

    "PRO",

    "PREMIUM",

    "ENTERPRISE"
]

settings = Settings()