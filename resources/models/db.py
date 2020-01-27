from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from aparcamalaga.settings import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=create_engine(SQLALCHEMY_DATABASE_URI)))
