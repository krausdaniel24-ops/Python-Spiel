from auth import login, register 
from database import init_db



def main():
    init_db()
    while True:
        print("1 = Einloggen, 2 = Registrieren")
        menu = input("Wählen sie zwischen 1 oder 2 aus: ")
        

        if menu == "1":
            username = login()
            print(f"Willkommen, {username}!")
            break

        elif menu == "2":
            register()

        else:
            print("Geben Sie bitte eine gültige Menüeingabe ein (1 oder 2).")


if __name__ == "__main__":
    main()



