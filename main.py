from auth import login, register 

def main():
    while True:
        print("1 = Einloggen, 2 = Registrieren")
        menu = int(input("Wählen sie zwischen 1 oder 2 aus: "))

        if menu == 1:
            username = login()
            print(f"Willkommen, {username}!")
            break

        elif menu == 2:
            register()

        else:
            print("Geben Sie bitte eine gültige Menüeingabe ein.")


if __name__ == "__main__":
    main()



