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
    episodes = int(input("Entrer le nombre d'épisodes :"))
    author = input("Entrer le nom de l'autheur :")
    cover = input("Entrer le lien du cover :")
    trailer = input("Entrer le lien du trailer :")

    data = {
        "title": title,
        "release_date": release_date,
        "episodes": episodes,
        "author": author,
        "cover": cover,
        "trailer": trailer
    }
    storage.child("animes").child(_id).set(data)
    print("Ajouter avec succès !")


def read():
    anime = storage.child("animes").get().val()
    print(anime)


def menu():
    while True :
        print("Option :")
        print("Entrer 1 pour ajouter un animé ")
        print("Entrer 2 pour voir les animés existant")
        print("Entrer 3 pour quitter")
        option = int(input("choisissez une option :"))
        if option == 1 :
            create()
        elif option == 2 :
            read()
        elif option == 3:
            print("Astala vista ...")
            break
        else:
            print("Option non disponible")


menu()