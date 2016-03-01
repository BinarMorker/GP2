'''
@author: Marc-Antoine Renaud et François Allard
'''

class Nombre(object):
    '''
    Outils de validation supplémentaires sur les nombres 
    '''
    
    @staticmethod
    def is_float(number):
        '''
        Vérifie si le nombre est un float
        @param number: Nombre à vérifier
        @return: Vrai si le nombre est un float
        '''
        try:
            float(number)
            return True
        except ValueError:
            return False