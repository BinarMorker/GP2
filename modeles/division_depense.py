from sqlalchemy import *
from sqlalchemy.orm import relationship, backref

from modeles.base import Base

class Division_Depense(Base):
    '''
    classdocs
    '''
    
    __tablename__ = "Divisions_Depenses"
    id_depense = Column(INTEGER, ForeignKey('Depenses.id'), primary_key=True)
    id_entite = Column(INTEGER, ForeignKey('Entites.id'), primary_key=True)
    pourcentage = Column(INTEGER)
    montant_paye = Column(FLOAT)
    
    depense = relationship("Depense", 
                           foreign_keys=[id_depense], 
                           backref=backref("divisions_depenses", 
                                           uselist=True
                                           )
                           )
    entite = relationship("Entite", 
                          foreign_keys=[id_entite], 
                          backref=backref("divisions_depenses", 
                                          uselist=True
                                          )
                          )
    
    def montant_total(self):
        return self.depense.montant*self.pourcentage/100
    
    def montant_a_payer(self):
        return self.montant_total()-self.montant_paye
    
    def est_paye(self):
        if self.montant_a_payer <= 0:
            return True
        else:
            return False
            