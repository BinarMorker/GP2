from models.depense import *

class DepensesControlleur(object):

	def voir_depenses():
		depenses = set()
		i = 0

		while (i < 10):
			obj = Depense('Allo'+str(i), i)
			depenses.add(obj)
			i += 1
			print(obj.nom)

	def ajouter_depense():
		print('À venir')