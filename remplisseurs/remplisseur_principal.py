from modeles.base import *

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from remplisseurs.remplisseur_depenses import remplir_depenses
from remplisseurs.remplisseur_entites import remplir_entites
from remplisseurs.remplisseur_categories import remplir_categories

engine = create_engine("sqlite:///sources//basededonnee.db", encoding="utf8", convert_unicode=True)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
s = session()

remplir_entites(s)
remplir_depenses(s)
remplir_categories(s)