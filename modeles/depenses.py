'''
Created on 2016-02-23

@author: Jeremi Pedneault
'''
from sqlalchemy import *
from modeles import Base

class Depense(Base):
    '''
    classdocs
    '''
    
    __tablename__ = "Depenses"
    id = Column(INTEGER, primary_key=True)
    nom = Column(String)
    description = Column(String, nullable = True)
    montant = Column(float)