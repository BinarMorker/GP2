'''
Created on 2016-02-23

@author: Jeremi Pedneault
'''
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from modeles.distribution_depense import Distribution_Depense

from modeles.base import Base


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
                           backref=backref("depenses", 
                                           uselist=True
                                           )
                           )