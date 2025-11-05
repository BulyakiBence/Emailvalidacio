def validate_email(email):
    # 1. At least one '@'
    if '@' not in email:
        print("An email address has to contain a '@' character!")
        return

    # 2. Only one '@'
    if email.count('@') > 1:
        print("An email address cannot contain more than one '@' characters!")
        return

    username, domain = email.split('@')

    # 3. Username is not empty
    if username == "":
        print("The username before the '@' character cannot be empty!")
        return

    # 4. Domain is not empty
    if domain == "":
        print("The domain after the '@' character cannot be empty!")
        return

    # 5. At least one '.'
    if '.' not in email:
        print("An email address has to contain at least one '.' character!")
        return

    # 6. At least one '.' in domain
    if '.' not in domain:
        print("The domain has to contain at least one '.' character!")
        return

    # 7. Top-level domain is not empty
    if domain.endswith('.'):
        print("The top-level domain cannot be empty!")
        return

    # 8. TLD is at least two characters long
    tld = domain.split('.')[-1]
    if len(tld) < 2:
        print("The top-level domain has to be at least two characters long!")
        return

    # 9. Valid username
    if username.startswith('.'):
        print("The username cannot start with a '.' character!")
        return

    # 10. Valid server name
    if domain.startswith('.'):
        print("The domain cannot start with a '.' character!")
        return

    # 11. Valid email address
    print("Valid email address :)")


# --- Tesztelés ---
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

for e in test_emails:
    print(f"Testing: {e}")
    validate_email(e)
    print("-" * 50)
