import requests
from sys import exit
import string
import random
from bs4 import BeautifulSoup

def get_fake_email():
    url = 'https://email-fake.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    mail = soup.find_all("span", {"id": "email_ch_text"})
    return mail[0].contents[0]

def generate_password():
    longueur = random.randint(8, 10)

    caracteres = string.ascii_letters + string.digits
    mot_de_passe = random.choice(string.ascii_uppercase) + random.choice(string.digits)
    mot_de_passe += ''.join(random.choice(caracteres) for _ in range(longueur - 2))
    mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))

    return mot_de_passe

def generate_user():
    url = "https://randomuser.me/api/"
    result = requests.get(url)

    if result.status_code == 200:
        personne = result.json()
        user = {}
        user["prenom"] = personne["results"][0]["name"]["first"]
        user["nom"] = personne['results'][0]['name']['last']
        user["email"] = get_fake_email()
        user["username"] = personne['results'][0]['login']['username']
        user["password"] = generate_password()
        print(user)
        return user
    else:
        print("erreur api : randomuser.me/api")
        exit()


generate_user()