from sqlalchemy import *
from sqlalchemy.orm import relationship, backref

from modeles.base import Base

class Distribution_Depense(Base):
    '''
    classdocs
    '''
    
    __tablename__ = "Distributions_Depenses"
    id_depense = Column(INTEGER, ForeignKey('Depenses.id'), primary_key=True)
    id_membre = Column(INTEGER, ForeignKey('Membres.id'), primary_key=True)
    pourcentage = Column(INTEGER)
    montant_paye = Column(FLOAT)
    
    depense = relationship("Depense", 
                           foreign_keys=[id_depense], 
                           backref=backref("distributions", 
                                           uselist=True
                                           )
                           )
    membre = relationship("Membre", 
                          foreign_keys=[id_membre], 
                          backref=backref("distributions", 
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
            