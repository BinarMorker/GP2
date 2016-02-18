# -*- coding: utf8 -*-
"""
Simon Truchon Brouillette
Travail final BD1
Menus
2014-04-07
"""

import sys
import Requetes

def menu_principal():
    '''Affiche le menu principal'''
    while True:
        print("Que voulez-vous faire?",
              "\n    1 - Transactions"
              "\n    2 - Informations",
              "\n    3 - Gestion",
              "\n    0 - Quitter")
        options = {'1': lambda: menu_transactions(),
                   '2': lambda: menu_informations(),
                   '3': lambda: menu_gestion(),
                   '0': lambda: sys.exit(0)}
        choix = valider_choix(4)
        options[choix]()
        print("")

#----------Verifications

def valider_choix(nb_options):
    '''
    Gere les entrees au clavier pour les menus.
    Boucle tant que l'entree n'est pas entre 0 et nb_options.
    Retourne l'entree fructueuse.
    '''
    options = [str(i) for i in range(nb_options)]
    choix = input("    Choix: ")
    while choix not in options:
        print("Entree invalide.")
        choix = input("    Choix: ")
    return(choix)

def numero_client():
    '''
    Gere l'entree d'un numero de client.
    Renvoie le numero s'il est valide et Faux autrement.
    '''
    client = input("\nNumero du client: ")
    while not client.isdigit() and client != "":
        print("Entree invalide.\nRecommencez ou n'entrez rien pour annuler.")
    if client == "" or not Requetes.client_existe(client):
        client = False
    return(client)

def numero_video():
    '''
    Gere l'entree d'un numero de video.
    Renvoie le numero s'il est valide et Faux autrement.
    S'assure que la video est disponible a la location.
    '''
    video = input("\nNumero de la video: ")
    etat = Requetes.etat_video(video)
    while video != "" and ( not video.isdigit() or etat != 'D' ):
        if not video.isdigit():
            print("Entree invalide.\nRecommencez",
                  "ou n'entrez rien pour terminer.")
        elif etat != 'D':
            print("Cette video n'est pas disponible actuellement.")
        video = input("\nNumero de la video: ")
        etat = Requetes.etat_video(video)
    if video == "":
        video = False
    else:
        video = int(video)
    return(video)

#----------Mises a jour

def menu_transactions():
    '''Affiche les options relatives aux transactions'''
    choix = True
    while choix != '0':
        print("Quelle est la transaction a effectuer?",
              "\n    1 - Location"
              "\n    2 - Retour",
              "\n    0 - Quitter")
        options = {'1': lambda: location(),
                   '2': lambda: retour(),
                   '0': lambda: False}
        choix = valider_choix(3)
        options[choix]()
        print("")
    return

def location():
    '''
    Marque la location d'une video
    Cree un nouveau client s'il y a lieu
    '''
    print("Le client a-t-il un compte?\n    1 - Oui"\
          "\n    0 - Non"\
          "\n Rien - Annuler")
    compte = input("    ")
    while compte not in ['1', '0', '']:
        print("Entree invalide.\nRecommencez ou n'entrez rien pour annuler.")
    if compte != '':
        client = False
        if compte == '1':
            client = numero_client()
        elif compte == '0':
            client = ajout_client()
        if client:
            videos = []
            video = numero_video()
            while video:
                videos += [video]
                video = numero_video()
            if videos != []:
                paie = input("\nType de paiement (C/A/D): ")
                while paie not in ['C', 'A', 'D', '']:
                    print("Entree invalide.\nRecommencez",
                          "ou n'entrez rien pour annuler.")
                    paie = input("\nType de paiement (C/A/D): ")
                if paie != "":
                    com = input("Commentaire, s'il y a lieu: ")
                    if com == "":
                        com = None
                    facture = Requetes.creer_facture(client, videos, paie, com)
                    Requetes.creer_location(videos, facture)
    return

def retour():
    '''
    Marque le retour d'une video, indique les retards
        et offre de les faire payer tout de suite
    '''
    Requetes.verifier_retards()
    video = numero_video()
    while video:
        if Requetes.etat_video(video) == 'S':
            if Requetes.location_en_retard(video):
                print("Cette video est en retard."          \
                      "\n    1 - Payer le retard maintenant"\
                      "\n    0 - Payer le retard plus tard" )
                retardPaye = valider_choix(2)
                if retardPaye == 1:
                    Requetes.payer_retard(video)
            Requetes.changer_etat_location(video, 'R')
        else:
            print("Cette video ne semble pas avoir ete louee.")
        video = numero_video()
    return

#----------Affichage

def menu_informations():
    '''Affiche les options relatives à l'affichage d'information'''
    choix = True
    while choix != '0':
        print("\nQue voulez-vous afficher?",
              "\n    1 - Client par nom",
              "\n    2 - Client par Id",
              "\n    3 - Toutes les videos",
              "\n    4 - Videos par annee",
              "\n    5 - Videos par genre",
              "\n    6 - Facture par Id",
              "\n    7 - Clients en retard",
              "\n    8 - Locations par mois",
              "\n    9 - Locations par client",
              "\n   10 - Palmares des locations",
              "\n    0 - Retour")
        options = {'1': lambda: client_par_nom(),
                   '2': lambda: client_par_id(),
                   '3': lambda: Requetes.videos(),
                   '4': lambda: videos_par_annee(),
                   '5': lambda: videos_par_genre(),
                   '6': lambda: facture_par_id(),
                   '7': lambda: Requetes.clients_en_retard(),
                   '8': lambda: locations_par_mois(),
                   '9': lambda: locations_par_client(),
                  '10': lambda: palmares(),
                   '0': lambda: False}
        choix = valider_choix(11)
        options[choix]()
    return

def client_par_nom():
    '''Affiche les clients portant un prenom et/ou un nom donnes'''
    print("\nVous pouvez laisser les deux prochains champs vides"\
          "\npour ne pas en tenir compte au cours de la recherche")
    prenom = input("\nPrenom: ")
    nom = input("Nom:    ")
    Requetes.client_par_nom(prenom, nom)
    return

def client_par_id():
    '''Affiche un client pour un id donne'''
    client = input("\nNumero du client: ")
    while not client.isdigit() and client != "":
        print("Entree invalide.\nRecommencez ou n'entrez rien pour annuler.")
        client = input("\nNumero du client: ")
    if client != "":    
        client = int(client)
        Requetes.client_par_id(client)
    return

def videos_par_annee():
    '''Affiche les films produits durant une annee donnee'''
    annee = input("\nAnnee de production: ")
    while not annee.isdigit() and annee != "":
        print("Entree invalide.\nRecommencez ou n'entrez rien pour annuler.")
        annee = input("\nAnnee de production: ")
    if annee != "":    
        annee = int(annee)
        Requetes.videos_par_annee(annee)
    return

def videos_par_genre():
    '''Affiche les films appartenant a un genre donne'''
    genre = input("\nGenre de films a afficher: ")
    if genre != "":
        Requetes.videos_par_genre(genre)
    return

def facture_par_id():
    '''Affiche une facture pour un numero donne'''
    facture = input("\nNumero de la facture: ")
    while not facture.isdigit() and facture != "":
        print("Entree invalide.\nRecommencez ou n'entrez rien pour annuler.")
        facture = input("\nNumero de la facture: ")
    if facture != "":    
        facture = int(facture)
        Requetes.facture_par_numero(facture)
    return

def locations_par_mois():
    '''Affiche le montant total des locations pour une periode'''
    options_mois = [str(i).rjust(2,'0') for i in range(13)]
    print("\nVous pouvez laisser les deux prochains champs vides"\
          "\npour ne pas en tenir compte au cours de la recherche")
    mois = input("\nMois (01-12):  ")
    annee = input("Annee       : ")
    if len(mois) == 1:
        mois = mois.rjust(2, '0')
    while mois not in options_mois and "" not in [mois, annee]:
        print("Entree invalide.\nRecommencez ou n'entrez rien pour annuler.")
        mois = input("\nMois:  ")
        annee = input("Annee: ")
    Requetes.locations_par_mois(mois, annee)
    return

def locations_par_client():
    '''Affiche les montant total des locations d'un client'''
    client = input("\nNumero du client: ")
    while not client.isdigit() and client != "":
        print("Entree invalide.\nRecommencez ou n'entrez rien pour annuler.")
        client = input("\nNumero du client: ")
    if client != "":    
        client = int(client)
        Requetes.locations_par_client(client)
    return

def palmares():
    '''Affiche les videos s'etant le plus loue'''
    nombre = input("\nCombien faut-il afficher de resultats?\n    ")
    while not nombre.isdigit() and nombre != "":
        print("Entree invalide.\nRecommencez ou n'entrez rien pour annuler.")
        nombre = input("\nCombien faut-il afficher de resultats?\n    ")
    if nombre != "":    
        nombre = int(nombre)
        Requetes.palmares(nombre)
    return

#----------Creation

def menu_gestion():
    '''Affiche les options relatives aux créations'''
    choix = True
    while choix != '0':
        print("Que voulez-vous faire?",
              "\n    1 - Ajout d'un client"
              "\n    2 - Ajout d'un film",
              "\n    3 - Ajout d'une video",
              "\n    0 - Retour")
        options = {'1': lambda: ajout_client(),
                   '2': lambda: ajout_film(),
                   '3': lambda: ajout_video(),
                   '0': lambda: False}
        choix = valider_choix(4)
        options[choix]()
        print("")
    return

def ajout_client():
    '''Cree un nouveau client dans la base de donnees'''
    print("\nLaisser un des 5 champs suivants vide annulera la location.")
    valide = False
    prenom = input("Prenom: ")
    if prenom != "":
        nom = input("Nom:    ")
        if nom != "":
            telephone = input("Numero de telephone: ")
            if telephone != "":
                dateN = input("Date de naissance: ")
                if dateN != "":
                    sexe = input("Sexe:   ")
                    if sexe != "":
                        valide = True
    if valide:
        client = Requetes.creer_client(prenom, nom, telephone, dateN, sexe)
    else:
        client = False
    return(client)

def ajout_film():
    '''Cree un nouveau film dans la base de donnees'''
    print("\nLaisser un des 5 champs suivants vide annulera la creation.")
    valide = False
    titre = input("Titre:  ")
    if titre != "":
        annee = input("Annee de production: ")
        while not (annee.isdigit() or annee == ""):
            print("Entree invalide.\nRecommencez",
                  "ou n'entrez rien pour annuler.")
            annee = input("Annee de production: ")
        if annee != "":
            annee = int(annee)
            real = input("Id du realisateur: ")
            while not ( real == "" or                         \
                       ( real.isdigit() and                   \
                         Requetes.realisateur_existe(real) ) ):
                print("Entree invalide.\nRecommencez",
                      "ou n'entrez rien pour annuler.")
                real = input("Id du realisateur: ")
            if real != "":
                real = int(real)
                langue = input("Langue: ")
                if langue != "":
                    print("Le champ suivant peut être laissé vide.")
                    titreO = input("Titre original: ")
                    if titreO == "":
                        titreO = None
                    genre = input("Genre:  ")
                    if genre != "":
                        if genre not in Requetes.genres():
                            genre = Requetes.creer_genre(genre)
                        else:
                            genre = Requetes.id_genre(genre)
                        valide = True
    if valide:
        film = Requetes.creer_film(titre, annee, real, langue, titreO)
        Requetes.associer_genre(film, genre)
    return

def ajout_video():
    '''Cree une nouvelle video dans la base de donnees'''
    print("\nLaisser un des 5 champs suivants vide annulera la creation.")
    valide = False
    film = input("Id du film:  ")
    while film != "" and not(film.isdigit() and Requetes.film_existe(film)):
        film = input("Id du film:  ")
        print("Entree invalide.\nRecommencez",
              "ou n'entrez rien pour annuler.")
    if film != "":
        film = int(film)
        typeV = input("Format (D/B/V): ")
        while typeV not in ['d','D','b','B','b','V', '']:
            print("Entree invalide.\nRecommencez",
                  "ou n'entrez rien pour annuler.")
            typeV = input("Format (D/B/V): ")
        if typeV != "":
            typeV = typeV.upper()
            prix = input("Prix (¢): ")
            while not (prix.isdigit() or prix == ""):
                print("Entree invalide.\nRecommencez",
                      "ou n'entrez rien pour annuler.")
                print(input("Prix (¢): "))
            if prix != "":
                prix = int(prix)
                duree = input("Duree de location: ")
                while duree != "" and not duree.isdigit():
                    print("Entree invalide.\nRecommencez",
                          "ou n'entrez rien pour annuler.")
                    duree = input("Duree de location: ")
                if duree != "":
                    duree = int(duree)
                    valide = True
    if valide:
        Requetes.creer_video('D', prix, film, typeV, duree)
    return