from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from outils.singleton import Singleton

@Singleton
class BaseDeDonnees:
    
    session = None
    
    def __init__(self):
        engine = create_engine("sqlite:///sources//basededonnee.db", encoding="utf8", convert_unicode=True)
        session = sessionmaker(bind=engine)
        self.session = session()