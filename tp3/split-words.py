import re
import ast # usada para converter string para dicionário na função loadNGrama()
import threading
# import unidecode

class Solution (threading.Thread):

    def __init__(self, id, ngrama, text):
        threading.Thread.__init__(self)
        self.id = id
        self.ngrama = ngrama
        self.text = text

    def run(self):
        tmp_key = ""
        for key in self.ngrama:
            tmp_key = re.sub("\ ", "", key)
            self.text = re.sub(tmp_key, key, self.text)
        print("Thread " + self.id + ": " + self.text)

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
    Solution.treino("files/files-to-training/portuguese-training.txt", "files/ngrams/ngrama", 2, sort=True)
    ngrama = Solution.loadNGrama("files/ngrams/ngrama")
    fileNames = ["ElefoicomeracasadoCarlos", "Eladissequesim"]
    N_THREADS = len(fileNames)
    threads = [] # arrays de threads

    for i in range(N_THREADS):
        s = Solution(str(i), ngrama, fileNames[i])
        threads.append(s)
        s.start()

main()
