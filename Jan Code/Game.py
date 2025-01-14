import sqlite3
from Database import initialize_database
from Anmeldung import  not_logged_in_user

initialize_database()

def main_menu():
        not_logged_in_user()

main_menu()