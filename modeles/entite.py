'''
Created on 2016-02-24

@author: Steve Lehoux
'''
from sqlalchemy import *
from modeles.base import Base

class Entite(Base):
    '''
    classdocs
    '''
    
    __tablename__ = "Entites"
    id = Column(INTEGER, primary_key=True)
    nom = Column(String)