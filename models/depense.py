class Depense(object):
	"""docstring for Depense"""

	id = 0
	nom = ""
	description = ""
	categorie = ""
	montant = 0.0

	def __init__(self, nom, montant, categorie = "", description = ""):
		self.nom = nom
		self.description = description
		self.categorie = categorie
		self.description = description