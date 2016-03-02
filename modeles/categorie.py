'''
Created on 2016-02-24

@author: Steve Lehoux
'''
from sqlalchemy import *
from modeles.base import Base

class Categorie(Base):
    '''
    classdocs
    '''
    
    __tablename__ = "Categories"
    id = Column(INTEGER, primary_key=True)
    nom = Column(String)
    description = Column(String)