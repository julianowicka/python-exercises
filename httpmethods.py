import requests

api_url = "https://reqres.in/api/"

def show_users(page=1):
    """Funkcja wyświetla listę użytkowników z podanej strony.
    Dla każdego użytkownika wyświetlany jest: adres e-mail, imię oraz nazwisko.

    Argumenty:
        page - numer strony, z której pobierani są użytkownicy.
    """
    response = requests.get(f"{api_url}users", params={"page": page})
    if response.status_code == 200:
        data = response.json()
        users_list = data["data"]
        for user in users_list:
            print(f"{user['email']} {user['first_name']} {user['last_name']}")
    else:
        print(f"Nie udało się pobrać danych. Status: {response.status_code}")


def show_user(user_id=1):
    """Funkcja wyświetla adres e-mail, imię oraz nazwisko użytkownika o zadanym identyfikatorze.
    Jeżeli użytkownik nie istnieje, funkcja wyświetla stosowny komunikat.

    Argumenty:
        user_id - identyfikator użytkownika do wyświetlenia.
    """
    response = requests.get(f"{api_url}users/{user_id}")
    if response.status_code == 200:
        data = response.json()
        user = data["data"]
        print(f"{user['email']} {user['first_name']} {user['last_name']}")
    else:
        print(f"Nie udało się pobrać danych. Status: {response.status_code}")


def register_user(email="eve.holt@reqres.in", password="pass"):
    """Funkcja rejestruje nowego użytkownika używając podanych danych.
    Po rejestracji wyświetlany jest identyfikator użytkownika oraz token autoryzacyjny.
    W przypadku błędu wyświetlany jest stosowny komunikat.

    Argumenty:
        email - adres e-mail nowego użytkownika.
        password - hasło nowego użytkownika.
    """
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f"{api_url}register", data=data)

    if response.status_code == 200:
        user_id = response.json()['id']
        token = response.json()['token']
        print(f"Zarejestrowano użytkownika o id {user_id}. Token: {token}")
    else:
        print(f"Nie udało się zarejestrować użytkownika. Error: {response.json()['error']}")

def login_user(email="eve.holt@reqres.in", password="pass"):
    """Funkcja logująca użytkownika na serwerze.
    Po zalogowaniu wyświetlany jest token autoryzacyjny.
    W przypadku błędu wyświetlany jest stosowny komunikat.

    Argumenty:
        email - adres e-mail użytkownika.
        password - hasło użytkownika.
    """
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f"{api_url}login", data=data)

    if response.status_code == 200:
        token = response.json()['token']
        print(f"Zalogowano użytkownika. Token: {token}")
    else:
        print(f"Nie udało się zalogować użytkownika. Error: {response.json()['error']}")


def delete_user(user_id=1):
    """Funkcja usuwa wybranego użytkownika.
    Wyświetlana jest informacja o powodzeniu (lub nie) operacji.

    Argumenty:
        user_id - identyfikator użytkownika do usunięcia.
    """
    response = requests.delete(f"{api_url}users/{user_id}")
    if response.status_code == 204:
        print("Użytkownik usunięty.")
    else:
        print(f"Nie udało się usunąć użytkownika. Status: {response.status_code}")

print("""Wybierz opcję:
1 - pokaż listę użytkowników
2 - pokaż wybranego użytkownika
3 - zarejestruj nowego użytkownika
4 - zaloguj użytkownika
5 - usuń użytkownika
""")

option = int(input("Wybrana opcja: "))

if option == 1:
    show_users()
elif option == 2:
    show_user()
elif option == 3:
    register_user()
elif option == 4:
    login_user()
elif option == 5:
    delete_user()
else:
    print("Błędna opcja!")