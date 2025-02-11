from envparse import Env

env = Env()

SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
ALGORITHM: str = env.str("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=1440)


DATABASE_URL = "postgresql+asyncpg://postgres:admin123@localhost/crm_repid_db"

DATABASE_URL_TEST = "postgresql+asyncpg://postgres:admin123@localhost/crm_repid_test_db"