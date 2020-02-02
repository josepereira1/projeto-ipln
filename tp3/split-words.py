#!/usr/bin/python3
import re
import ast # usada para converter string para dicionário na função loadNGrama()
import threading
from getopt import getopt
import sys
import fileinput
# import unidecode

class Solution (threading.Thread):

    def __init__(self, id, ngrama, filename):
        threading.Thread.__init__(self)
        self.id = id
        self.ngrama = ngrama
        self.filename = filename

    def run(self):
        print(f"Start Thread {self.id} ...")
        text = ""

        for line in fileinput.input(self.filename):
            text += line

        tmp_key = ""
        for key in self.ngrama:
            tmp_key = re.sub("\ ", "", key)
            text = re.sub(tmp_key, key, text)

        f = open(self.filename, "w")
        f.write(text)
        f.close()

        print(f"End of Thread {self.id} ...")


    def nGrama(text, N):
        counter = {}
        # text = unidecode.unidecode(text) # remove acentos => unidecode("olá") = "ola"
        # text = text.lower() # obtem o texto todo em mínusculas
        words = re.findall(r"[\wÀ-Üà-ü]+", text) # obtem as palavras do texto (removendo pontuação, espaços, etc)
        for i in range(len(words)-N+1):
            ngrama = ""
            for k in range(N):
                ngrama = ngrama + " " + words[i+k]
            ngrama = ngrama[1::]    # para remover o espaço inicial
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
    def treino(input, output, N, sort):
        fileInput = open(input, "r", encoding='utf-8')
        text = fileInput.read()
        fileInput.close()
        ngrama = Solution.nGrama(text, N)
        if sort:
            ngrama = dict(sorted(ngrama.items(), key=lambda item: item[1], reverse = True))
        Solution.saveNGrama(ngrama, output) # escreve o n-grama no ficheiro output


def main():
    opts, resto = getopt(sys.argv[1:],"help:h:t:f:")
    print(len(sys.argv))

    if len(sys.argv) > 3:
        print("Error! Only one argument!")
        sys.exit(1)

    if opts[0][0] == "-h":  #   HELP
        print("HELP!")
        sys.exit(1)

    filenames = []

    if opts[0][0] == "-t":
        print("Start ...")
        filenames = opts[0][1].split(',')
        Solution.treino(filenames[0], filenames[1], 2, sort=True)
        print("End!")
        sys.exit(1)

    if opts[0][0] == "-f":
        filenames = opts[0][1].split(',')
        ngramDir = "files/ngrams/ngrama"
        ngrama = Solution.loadNGrama(ngramDir)

        threads = [] # arrays de threads

        for i in range(len(filenames)):
            s = Solution(str(i), ngrama, filenames[i])
            threads.append(s)
            s.start()


main()

