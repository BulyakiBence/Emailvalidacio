def validate_email(email):
    if '@' not in email:
        print("Az emailben lennie kell @-nak!")
        return

    if email.count('@') > 1:
        print("Egy emailben nem lehet egynél tóbb @!")
        return

    username, domain = email.split('@')

    if username == "":
        print("A felhasználónév a @ előtt nem lehet üres!")
        return

    if domain == "":
        print("A domain a @ után nem lehet üres!")
        return

    if '.' not in email:
        print("Hiányzik a . az emailból!")
        return

    if '.' not in domain:
        print("A domainből hiányzik a .!")
        return

    if domain.endswith('.'):
        print("A top-level domain vége nem lehet üres!")
        return

    
    tld = domain.split('.')[-1]
    if len(tld) < 2:
        print("A top-level domainnak minimum 2 karakter hosszúnak kell lennie!")
        return

    if username.startswith('.'):
        print("A felhasználónév nem kezdődhet .-tal!")
        return

    if domain.startswith('.'):
        print("A domain nem kezdődhet .-tal!")
        return
    
    print("Valid email cím :)")


''' --- Tesztelés ---
test_emails = [
    "hello.worldcom",        # nincs @
    "he@@llo@@worldcom",     # több @
    "@@world.com",           # üres username
    "hello@",                # üres domain
    "hello@@worldcom",       # nincs .
    "hell.o@@worldcom",      # domainben nincs .
    "hello@@worldcom.",      # üres TLD
    "hello@@worldco.m",      # TLD < 2 karakter
    ".hello@@world.com",     # username ponttal kezdődik
    "he.llo@.world.com",     # domain ponttal kezdődik
    "hello@world.com"        # helyes email
]
'''

'''
for e in test_emails:
    print(f"Testing: {e}")
    validate_email(e)
    print("-" * 50)
'''