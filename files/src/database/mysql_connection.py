import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(f'mysql+pymysql://{os.environ["MYSQL_USER"]}:{os.environ["MYSQL_PASSWORD"]}@{os.environ["MYSQL_HOST"]}/{os.environ["MYSQL_DB"]}')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))