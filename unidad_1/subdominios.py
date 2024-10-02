'''
programa para encontrar los  subdominios de un sitio.
explicar que hace este script.
desarrollado por Luis Alberto Rico Jimenez.
'''

import requests
from os import path
import argparse
import sys

# Definir los argumentos de línea de comandos
parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Indica el dominio del insecto')
args = parse.parse_args()

# Asignar el valor de args.target al objeto parse
parse.target = args.target

def main():
    if parse.target:  # Ahora puedes usar parse.target porque le asignamos el valor de args.target
        if path.exists('subdominios.txt'):
            with open('subdominios.txt', 'r') as wordlist:
                wordlist = wordlist.read().split('\n')

            for subdominio in wordlist:
                url = "http://" + subdominio + "." + parse.target
                #print(url)

                try:
                    requests.get(url, timeout=3)
                except requests.ConnectionError:
                    pass
                else:
                    print("Se encontró un subdominio: " + url)

        else:
            print("No se encontró el archivo 'subdominios.txt'")
    else:
        print("No se especificó un dominio objetivo")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()