
# 0. Bekérek egy email címet
email = input("Add meg az e-mail címet: ")

# 1. Legalább egy '@' karakter
if email.count('@') == 0:
    print("Kell minimum egy '@' az esmil címbe!")

# 2. Legfeljebb egy '@' karakter
elif email.count('@') > 1:
    print("EGy email címben nem lehet egynél több '@'!")

else:
    # Felbontom az e-mail címet a kukacnál
    username, domain = email.split('@')

    # 3. Felhasználónév nem lehet üres
    if username == "":
        print("A '@' előtti felhasználónév nem lehet üres!")

    # 4. Domain nem lehet üres
    elif domain == "":
        print("A '@' utáni domain nem lehet üres")

    # 5. Legalább egy '.' karakter az e-mailben
    elif '.' not in email:
        print("Minimum egy . kell egy email címbe!")

    # 6. Legalább egy '.' a domain részben
    elif '.' not in domain:
        print("A domainmben legalább egy .-nak kell lennie!")

    # 7. Domain nem végződhet '.'-ra
    elif domain.endswith('.'):
        print("A top-level domain nem végződhet .-ra!")

    else:
        # TLD (top-level domain) = az utolsó pont utáni rész
        tld = domain.split('.')[-1]

        # 8. TLD legalább 2 karakter hosszú
        if len(tld) < 2:
            print("A top-level domainnak minimum 2 karakter hosszúságúnak kell lennie!")

        # 9. Felhasználónév nem kezdődhet '.'
        elif username.startswith('.'):
            print("A felhasználónév nem kezdődhet .-tal!")

        # 10. Domain nem kezdődhet '.'
        elif domain.startswith('.'):
            print("A domain nem kezdődhet .-tal!")

        # 11. Ha minden rendben
        else:
            print("Valid email cím :)")
