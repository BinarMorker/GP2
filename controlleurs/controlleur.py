from sqlalchemy import create_engine, engine
from sqlalchemy.orm import relationship, backref, sessionmaker

class Controlleur(object):
    
    session = None
    
    def __init__(self):
        engine = create_engine("sqlite:///sources//basededonnee.db", encoding="utf8", convert_unicode=True)
        session = sessionmaker(bind=engine)
        self.session = session()