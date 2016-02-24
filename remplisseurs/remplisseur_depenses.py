from modeles.depenses import Depense
from modeles.base import *
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = create_engine("sqlite:///..//sources//basededonnee.db", encoding="utf8", convert_unicode=True)
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
s = session()


depense1 = Depense(
            nom = "McDo",
            description = "",
            montant = "54")

depense2 = Depense(
            nom = "Hydro-Quebec",
            description = "",
            montant = "120")

depense3 = Depense(
            nom = "La Capitale",
            description = "",
            montant = "250")

depense4 = Depense(
            nom = "Tim Hortons",
            description = "",
            montant = "40.75")

depense5 = Depense(
            nom = "Walt Mart",
            description = "",
            montant = "15")

depense6 = Depense(
            nom = "Costco",
            description = "",
            montant = "101.79")

depense7 = Depense(
            nom = "Shell",
            description = "",
            montant = "54")

depense8 = Depense(
            nom = "Irving",
            description = "",
            montant = "47.98")

depense9 = Depense(
            nom = "Ville",
            description = "",
            montant = "1012")

depense10 = Depense(
            nom = "Canadian Tire",
            description = "",
            montant = "15")
    
s.add_all([depense1, depense2, depense3, depense4, depense5, depense6, depense7, depense8, depense9, depense10])

s.commit()
