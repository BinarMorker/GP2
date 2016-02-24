'''
Created on 2016-02-23

@author: Jeremi Pedneault
'''
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref

from modeles.base import Base
from modeles.categorie import Categorie


class Depense(Base):
    '''
    classdocs
    '''
    
    __tablename__ = "Depenses"
    id = Column(INTEGER, primary_key=True)
    id_categorie = Column(INTEGER, ForeignKey("Categories.id"))
    nom = Column(String)
    description = Column(String, nullable = True)
    montant = Column(Float)
    
    categorie = relationship("Categorie", 
                           foreign_keys=[id_categorie], 
                           backref=backref("divisions_depense", 
                                           uselist=True
                                           )
                           )