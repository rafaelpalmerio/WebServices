from string import printable
from itertools import product

user_password = 'senha' # just a test password
found = False
caracteres = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

tries = 0
for length in range(1, 10): # it isn't reasonable to try a password more than this length
    #password_to_attempt = product(printable, repeat=length) #poderiamos usar todos, mas vamos usar so letras e numeros
    password_to_attempt = product(caracteres, repeat=length)
    for attempt in password_to_attempt:
        tries +=1
        attempt = ''.join(attempt) # <- Join letters together
        if tries % 10000000 == 0:
            print(tries, attempt)
        if attempt == user_password:
            print("Sua senha é: " + attempt)
            print("Foram necessárias ", tries," tentativas.")
            found = True
            break

    if found:
        break