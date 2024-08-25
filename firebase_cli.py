import json
from math import expm1

import pyrebase
import uuid

config = {
    "apiKey": "AIzaSyDt6axBji3MRusLNeRZZrCp_EfmuP6x80s",
    "authDomain": "pyanime-cli.firebaseapp.com",
    "projectId": "pyanime-cli",
    "storageBucket": "pyanime-cli.appspot.com",
    "messagingSenderId": "859056219481",
    "appId": "1:859056219481:web:1281e95cc6decbfbfcd848",
    "measurementId": "G-SD93FKS6KT",
    "serviceAccount": "newserviceAccount.json",
    "databaseURL": "https://pyanime-cli-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.database()


def create():
    _id = str(uuid.uuid4())
    title = input("Entrer le nom de l'animé :")
    release_date = input("Entrer la date de sortie de l'animé (yyyy-mm-dd) :")
    episodes = input("Entrer le nombre d'épisodes :")

    while not verify_integer(episodes):
        episodes = input("Entrer le nombre d'épisodes :")

    author = input("Entrer le nom de l'autheur :")
    cover = input("Entrer le lien du cover :")
    trailer = input("Entrer le lien du trailer :")

    data = {
        "title": title,
        "release_date": release_date,
        "episodes": episodes,
        "author": author,
        "cover": cover,
        "trailer": trailer,
    }
    storage.child("animes").child(_id).set(data)
    print("Ajouter avec succès !")


def read():
    animes = storage.child("animes").get().val()

    for anime in animes:
        print(33*"#")
        print(anime)

        print(
            json.dumps(
                storage.child('animes').child(anime).get().val(),
                indent=4
            )
        )
        print(33*"#")
        print("\n")



def update():
    _id = input("Entrer l'id de l'animé :")
    title = input("Entrer le nouveau titre :")
    release_date = input("Entrer la nouvelle date de sortie de l'animé (yyyy-mm-dd) :")
    episodes = int(input("Entrer le nouveau nombre d'épisodes :"))
    author = input("Entrer le nouveau nom de l'autheur :")
    cover = input("Entrer le nouveau lien du cover :")
    trailer = input("Entrer le nouveau lien du trailer :")

    update_data = {
        "title": title,
        "release_date": release_date,
        "episodes": episodes,
        "author": author,
        "cover": cover,
        "trailer": trailer,
    }

    for i in [j for j in update_data.keys()]:
        if not update_data[i]:
            del update_data[i]

    storage.child("animes").child(_id).update(update_data)
    print("Mise à jour avec success !")


def delete():
    _id = input("Entrer l'id pour supprimer :")
    storage.child("animes").child(_id).remove()
    print("Supprimé avec succès")


def menu():
    while True :
        print("Option :")
        print("Entrer 1 pour ajouter un animé ")
        print("Entrer 2 pour voir les animés existant")
        print("Entrer 3 pour une mise à jour ")
        print("Entrer 4 pour supprimer")
        print("Entrer 5 pour quitter")

        option = input("choisissez une option : ")

        if option == "1":
            create()
        elif option == "2":
            read()
        elif option == "3":
            update()
        elif option == "4":
            delete()
        elif option == "5":
            print("Astala vista ...")
            break
        else:
            print("Option non disponible")


def verify_integer(_input):
    try:
        return int(_input)

    except Exception:
        print(">>> ALERT : Tu dois utiliser un chiffre ou un nombre.")
        return False

menu()