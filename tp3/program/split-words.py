#!/usr/bin/python3
import re
import ast # usada para converter string para dicionário na função loadNGrama()
import threading
from getopt import getopt
import sys
# import unidecode


# static variables
output = "files/ngrams/ngrama"


class Solution (threading.Thread):

    def __init__(self, id, ngrama, filename):
        threading.Thread.__init__(self)
        self.id = id
        self.ngrama = ngrama
        self.filename = filename

    def run(self):
        print(f"Thread {self.id} started working on {self.filename}")

        text = open(self.filename).read()

        tmp_key = ""
        for key in self.ngrama:
            tmp_key = re.sub("\ ", "", key)
            text = re.sub(tmp_key, key, text)

        solfilename = self.filename + ".sw"
        f = open(solfilename, "w")
        f.write(text)
        f.close()

        print(f"Thread {self.id} wrote solution on {solfilename}")


    def nGrama(text, N, counter):
        # text = unidecode.unidecode(text) # remove acentos => unidecode("olá") = "ola"
        # text = text.lower() # obtem o texto todo em mínusculas
        words = re.findall(r"[\wÀ-Üà-ü]+", text) # obtém as palavras do texto (removendo pontuação, espaços, etc)
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
    def treino(filenames, N, sort):
        ngrama = {}

        for filename in filenames:
            file = open(filename, "r", encoding='utf-8')
            text = file.read()
            file.close()
            ngrama = Solution.nGrama(text, N, ngrama)

        if sort:
            ngrama = dict(sorted(ngrama.items(), key=lambda item: item[1], reverse = True))

        Solution.saveNGrama(ngrama, output) # escreve o n-grama no ficheiro output


def main():
    opts, resto = getopt(sys.argv[1:],"help:h:t:n:f:s:")

    if len(sys.argv) < 2:
        print("Too few of arguments.")
        sys.exit(1)

    elif opts[0][0] == "-h":
        if len(sys.argv) != 2:
            print("Incorret number of arguments.")
            sys.exit(1)
        print("split-words.py -h to display this (help) menu.")
        print("split-words.py -n [1,2,3,...] -s [0,1] -t \"file1,file2,...\" to get an N-gram from specified files.")
        print("split-words.py -f \"file1,file2,...\" to get the right text by spliting words.")
        sys.exit(1)

    elif opts[0][0] == "-n":
        if len(sys.argv) != 7:
            print("Incorret number of arguments.")
            sys.exit(1)
        filenames = []
        N = int(opts[0][1])
        sort = opts[1][1]
        if sort == "1": sort = True
        else: sort = False
        filenames = opts[2][1].split(',')
        print("Started tranning ...")
        Solution.treino(filenames, N, sort=sort)
        print("N-gram written to " + output)
        sys.exit(1)

    elif opts[0][0] == "-f":
        if len(sys.argv) != 3:
            print("Incorret number of arguments.")
            sys.exit(1)
        filenames = []
        filenames = opts[0][1].split(',')
        ngramafilename = output
        print("Loading N-gram from " + ngramafilename)
        ngrama = Solution.loadNGrama(ngramafilename)

        threads = [] # lista de threads
        for i in range(len(filenames)):
            s = Solution(str(i), ngrama, filenames[i]) # cria a Thread
            threads.append(s) # adiciona a Thread à lista
            s.start() # inicia o trabalho da Thread

        sys.exit(1)

    else:
        print("Shoud not get here...")

main()
