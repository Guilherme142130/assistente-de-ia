class Orientacao:
    def __init__(self, id, categoria, titulo, palavras_chave, resposta,
                 documentos, onde,fonte,verificado_em):
        self.id = id
        self.categoria = categoria
        self.titulo = titulo
        self.palavras_chave = palavras_chave
        self.resposta = resposta
        self.documentos = documentos
        self.onde = onde
        self.fonte = fonte
        self.verificado_em = verificado_em
  
    def exibir(self):
        print("\n" + "=" * 45)
        print(f"ID: {self.id}")
        print(f"Categoria: {self.categoria}")
        print(f"Título: {self.titulo}")

        print("\nResposta:")
        print(self.resposta)

        print("\nDocumentos necessários:")

        i = 0
        while i < len(self.documentos):
            print(f"- {self.documentos[i]}")
            i += 1

        print("\nOnde encontrar:")
        print(self.onde)

        print("\nFonte:")
        print(self.fonte)

        print(f"\nVerificado em: {self.verificado_em}")
        print("=" * 45)

      
 