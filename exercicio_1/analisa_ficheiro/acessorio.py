import os.path
def pede_nome():

    while True:
        nome = input("Insira o nome")
        ficheiro = nome + '.txt'
        if os.path.isfile(ficheiro):
            print(ficheiro)
            break
    
def gera_nome(ficheiro):
    primeiraParte = ficheiro.split(".")[0]
    return primeiraParte + '.json'
    

gera_nome("Beatriz.txt")
    