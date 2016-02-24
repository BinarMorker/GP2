from modeles.depenses import Depense
from modeles.base import *
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = create_engine("sqlite:///sources//basededonnee.db", encoding="utf8", convert_unicode=True)
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
s = session()

depense = Depense(
            nom = "Canadian Tire",
            description = "",
            montant = "15247.25")
    
s.add(depense)

s.commit()
