from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import setting

SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.database_username}:{setting.database_password}@' \
                          f'{setting.database_hostname}/{setting.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''while True:
    try:
        cnx = psycopg2.connect(host='localhost', database='Fastapi', user='postgres',
                            password='teravis5023717', cursor_factory=RealDictCursor)

        cursor=cnx.cursor()
        print("connection done")
        break

    except:
        print("could not connect !")
        time.sleep(2)'''