import re
import ast # usada para converter string para dicionário
# import unidecode

def nGrama(text, N):
    counter = {}
    # text = unidecode.unidecode(text) # remove acentos => unidecode("olá") = "ola"
    # text = text.lower() # obtem o texto todo em mínusculas
    words = re.findall(r"[\wÀ-Üà-ü]+", text) # obtem as palavras do texto (removendo pontuação, espaços, etc)
    for i in range(len(words)-N+1):
        ngrama = ""
        for k in range(N):
            ngrama = ngrama + " " + words[i+k]
        if ngrama not in counter: counter[ngrama] = 1
        else: counter[ngrama] += 1
    return counter

def saveNGrama(ngrama, filename):
    file = open(filename, "w")
    file.write( str(ngrama) )
    file.close()

def loadNGrama(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()
    return ast.literal_eval(text) # converte a string para dicionário


# Lê o texto de um ficheiro (input), calcula o N-grama e escreve o mesmo num ficheiro (output)
def treino(input, output, N):
    fileInput = open(input, "r", encoding='utf-8')
    text = fileInput.read()
    fileInput.close()
    ngrama = nGrama(text, N)
    saveNGrama(ngrama, output) # escreve o n-grama no ficheiro output

treino("texto.txt", "ngrama.txt", 10)
ngrama = loadNGrama("ngrama.txt")
# print(ngrama)
