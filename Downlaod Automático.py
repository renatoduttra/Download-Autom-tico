import os
import requests


def baixar_arquivo(url, endereco):
    # faz requisição ao servidor
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Donwload finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

if __name__ == "__main__":
    URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    DIRETORIO = r'C:\Users\Renato\Desktop\testes'
    for i in range(1, 26):
        nome_arquivo = os.path.join(DIRETORIO, 'nota_de_aula_{}.pdf'.format(i))
        baixar_arquivo(URL.format(i), nome_arquivo)