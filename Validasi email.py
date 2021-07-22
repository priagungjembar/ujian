import re

regex = r'\[A-Za-z0--9.0._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def validasiEmail(email):

    if(re.match(regex, email)):
        print("Email Valid")
    else:
        print("Email tidak valid")

    if __name__ == '__main__':
        email = input("Masukkan Email :")
        print("Data yang anda masukkan :", email)
validasiEmail(email)