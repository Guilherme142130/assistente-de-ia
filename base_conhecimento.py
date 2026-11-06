import json
from orientacao import Orientacao

ACENTOS = {
    'á': 'a','à': 'a',
    'ã': 'a','â': 'a',
    'é': 'e','ê': 'e',
    'í': 'i','ó': 'o',
    'ô': 'o','õ': 'o',
    'ú': 'u','ç': 'c'
}

def normalizar(texto):
    texto = texto.lower().strip()

    itens = list(ACENTOS.items())
    i = 0
    while i < len(itens):
        letra, troca = itens[i]
        texto = texto.replace(letra, troca)
        i += 1

    sinais = ".,;:!?()[]{}<>"
    i = 0
    while i < len(sinais):
        texto = texto.replace(sinais[i], " ")
        i += 1

    return " " + " ".join(texto.split()) + " "


class BaseConhecimento:
    def __init__(self, caminho):
        self.caminho = caminho
        self.orientacoes = []

    def carregar(self):
        try:
            with open(self.caminho, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

                i = 0
                while i < len(dados):
                    item = dados[i]
                    orientacao = Orientacao(
                        id=item['id'],
                        categoria=item['categoria'],
                        titulo=item['titulo'],
                        palavras_chave=item['palavras_chave'],
                        resposta=item['resposta'],
                        documentos=item['documentos'],
                        onde=item['onde'],
                        fonte=item['fonte'],
                        verificado_em=item['verificado_em']
                    )
                    self.orientacoes.append(orientacao)
                    i += 1

            print("Base de conhecimento carregada com sucesso!")

        except FileNotFoundError:
            print("Arquivo Não encontrado")

        except json.JSONDecodeError:
            print("Erro: o arquivo está inválido")

        except KeyError as erro:
            print(f"Erro: campo obrigatório ausente no JSON: {erro}")

    def categorias(self):
        categorias = []

        i = 0
        while i < len(self.orientacoes):
            orientacao = self.orientacoes[i]
            if orientacao.categoria not in categorias:
                categorias.append(orientacao.categoria)
            i += 1

        return categorias

    def por_categoria(self, categoria):
        resultado = []

        i = 0
        while i < len(self.orientacoes):
            orientacao = self.orientacoes[i]
            if orientacao.categoria.lower() == categoria.lower():
                resultado.append(orientacao)
            i += 1

        return resultado

    def pontuar(self, pergunta, orientacao):
        pontos = 0

        pergunta_normalizada = normalizar(pergunta)
        titulo_normalizado = normalizar(orientacao.titulo)

        i = 0
        while i < len(orientacao.palavras_chave):
            palavra = normalizar(orientacao.palavras_chave[i])

            if palavra in pergunta_normalizada:
                pontos += 3
            i += 1

        palavras = pergunta_normalizada.split()

        i = 0
        while i < len(palavras):
            palavra = palavras[i]
            if len(palavra) >= 4:
                if palavra in titulo_normalizado:
                    pontos += 1
            i += 1

        return pontos
    
    def buscar(self, pergunta):
        resultados = []

        i = 0
        while i < len(self.orientacoes):
            orientacao = self.orientacoes[i]
            pontos = self.pontuar(pergunta, orientacao)

            if pontos >= 3:
                resultados.append((pontos, orientacao))
            i += 1

        resultados.sort(key=lambda x: x[0], reverse=True)

        return resultados