from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = (
    "postgresql+psycopg2://postgres:Idiotdu81700"
    "@pfistrisklab.cfgg00o62wu6.eu-north-1.rds.amazonaws.com:5432/postgres"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False
)

def test_connection(engine):
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("OK")
    except SQLAlchemyError as e:
        print("Connexion failed")
        print(e)

if __name__ == "__main__":
    test_connection(engine)
