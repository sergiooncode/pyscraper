from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+pymysql://scraperuser:p@55w0rd@localhost:3307/python_scraper', echo=True)
Base = declarative_base()
Base.metadata.bind = engine
db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))
Base.query = db.query_property()
