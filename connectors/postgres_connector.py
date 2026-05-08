from sqlalchemy import create_engine

from pipeline.config.load_config import load_config


config = load_config()

db = config["postgres"]

DATABASE_URL = (
    f"postgresql://{db['user']}:"
    f"{db['password']}@"
    f"{db['host']}:"
    f"{db['port']}/"
    f"{db['database']}"
)

engine = create_engine(DATABASE_URL)