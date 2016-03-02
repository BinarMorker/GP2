'''
Created on 2016-02-24

@author: Steve Lehoux
'''
from sqlalchemy import *
from modeles.base import Base

class Membre(Base):
    '''
    classdocs
    '''
    
    __tablename__ = "Membres"
    id = Column(INTEGER, primary_key=True)
    nom = Column(String)