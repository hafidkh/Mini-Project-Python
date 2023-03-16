import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input('Entrez la longueur du mot de passe : '))
password = generate_password(length)
print(f'Votre mot de passe généré est : {password}')