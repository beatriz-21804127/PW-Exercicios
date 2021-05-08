"""calcula_linhas que recebe o nome do ficheiro e retorna o número de linhas do ficheiro
calcula_carateres que recebe o nome do ficheiro e retorna o número de carateres do ficheiro
calcula_palavra_comprida que retorna a palavra mais comprida do ficheiro.
calcula_ocorrencia_de_letras que recebe o nome do ficheiro e cria um dicionário de todas as letras do 
ficheiro, indicando a quantidade de vezes que cada letra ocorre. Deverá desprezar se é maiúscula ou minúscula.
 Por exemplo, para o ficheiro com conteúdo "Abracadabra, pura magia!" terá {"a":8, "b":2, "c":1, ...}"""

def calcula_linhas(nomeFicheiro):
    count = 0
    f = open(nomeFicheiro, "r")
    for linha in f:
        count = count +1
    f.close()
    return count
print(calcula_linhas("Beatriz.txt"))

def calcula_caracteres(nomeFicheiro):
    f = open(nomeFicheiro, "r")
    linhaUnica = f.read()
    numeroCaract = len(linhaUnica)
    f.close()
    return numeroCaract
print(calcula_caracteres("Beatriz.txt"))

def calcula_palavra_comprida(nomeFicheiro):
    f = open(nomeFicheiro, "r")
    linhaUnica = f.read().split()
    maior = len(max(linhaUnica, key=len))
    lista = [palavra for palavra in linhaUnica if len(palavra) == maior]
    return lista
print(calcula_palavra_comprida("Beatriz.txt"))


def calcula_ocorrencia_de_letras(nomeFicheiro):
    f = open(nomeFicheiro, "r")
    linhaUnica = f.read()
    lista = [letra.lower() for letra in linhaUnica]
    return {letra:lista.count(letra) for letra in set(lista) if letra.isalnum()}
print(calcula_ocorrencia_de_letras("Beatriz.txt"))


