import json
import csv
import time


class Assistente:
    def __init__(self, nome, base):
        self.nome = nome
        self.base = base
        self.historico = []
        self.carregar_historico()
        self.inicio_sessao = len(self.historico)

    def contem_dado_pessoal(self, texto):
        total_digitos = 0
        for caractere in texto:
            if caractere.isdigit():
                total_digitos += 1
        return total_digitos >= 8 or "@" in texto

    def ler_numero(self, maximo):
        while True:
            entrada = input("\nEscolha uma opção: ").strip()
            if entrada.isdigit() and int(entrada) <= maximo:
                return int(entrada)
            print("Opção inválida. Digite um número de 0 a", maximo)

    def ler_sim_nao(self, texto):
        while True:
            resposta = input(texto).strip().lower()
            resposta = resposta.replace("ã", "a")
            if resposta == "s" or resposta == "sim":
                return True
            if resposta == "n" or resposta == "nao":
                return False
            print("Digite s, sim, n ou não.")

    def ler_nota(self):
        while True:
            entrada = input("Nota de facilidade (1 a 5): ").strip()
            if entrada.isdigit() and 1 <= int(entrada) <= 5:
                return int(entrada)
            print("Digite um número de 1 a 5.")

    def mostrar_orientacao(self, orientacao):
        orientacao.exibir()
        print("Aviso: este assistente NÃO é um canal oficial.")

    def carregar_historico(self):
        try:
            with open("data/historico.json", "r", encoding="utf-8") as arquivo:
                self.historico = json.load(arquivo)
        except FileNotFoundError:
            self.historico = []
        except json.JSONDecodeError:
            print("Histórico com erro. Começando um novo.")
            self.historico = []

    def salvar_historico(self):
        try:
            with open("data/historico.json", "w", encoding="utf-8") as arquivo:
                json.dump(self.historico, arquivo, ensure_ascii=False, indent=4)
        except OSError:
            print("Não foi possível salvar o histórico.")

    def registrar(self, origem, pergunta, id_orientacao, encontrou, ajudou, tentativas, tempo):
        if self.contem_dado_pessoal(pergunta):
            return

        atendimento = {
            "data": time.strftime("%Y-%m-%d %H:%M:%S"),
            "origem": origem,
            "pergunta": pergunta,
            "id_orientacao": id_orientacao,
            "encontrou": encontrou,
            "ajudou": ajudou,
            "tentativas": tentativas,
            "tempo_segundos": tempo
        }
        self.historico.append(atendimento)
        self.salvar_historico()

    def perguntar(self):
        print("\n" + "=" * 45)
        print(f"Olá! Eu sou o {self.nome}.")
        print("Estou aqui para ajudar você!")
        print("=" * 45)

        tentativas = 0
        inicio = 0
        encontrou = False
        id_orientacao = None
        ultima_pergunta = ""

        while True:
            pergunta = input("\nDigite sua dúvida (0 para voltar): ")

            if pergunta.strip() == "0":
                if tentativas > 0:
                    tempo = round(time.time() - inicio, 1)
                    self.registrar("pergunta", ultima_pergunta, id_orientacao, encontrou, False, tentativas, tempo)
                print("\nVoltando ao menu...")
                break

            if pergunta.strip() == "":
                print("\nVocê precisa digitar uma pergunta.")
                continue

            if self.contem_dado_pessoal(pergunta):
                print("\nAtenção: não digite CPF, telefone ou e-mail. Reescreva.")
                continue

            if tentativas == 0:
                inicio = time.time()
            tentativas += 1
            ultima_pergunta = pergunta.strip()

            resultados = self.base.buscar(pergunta)

            if len(resultados) > 0:
                encontrou = True
                pontos, orientacao = resultados[0]
                id_orientacao = orientacao.id

                if pontos >= 6:
                    confianca = "ALTA"
                else:
                    confianca = "MÉDIA"

                print(f"\nConfiança da resposta: {confianca}")
                print(f"Pontuação: {pontos}")

                self.mostrar_orientacao(orientacao)

                alternativas = resultados[1:3]
                if len(alternativas) > 0:
                    print("\nOutras orientações que podem ajudar:")
                    for pts, alt in alternativas:
                        print(f"- {alt.titulo} [{alt.categoria}] ({pts} pontos)")

                ajudou = self.ler_sim_nao("\nEssa orientação respondeu sua dúvida? (s/n): ")

                if ajudou:
                    tempo = round(time.time() - inicio, 1)
                    self.registrar("pergunta", ultima_pergunta, id_orientacao, True, True, tentativas, tempo)
                    print("\nQue bom que ajudou!")
                    tentativas = 0
                    encontrou = False
                    id_orientacao = None
                    ultima_pergunta = ""
                else:
                    print("\nTente escrever sua dúvida com outras palavras.")

            else:
                print("\nNão encontrei uma orientação para sua dúvida.")
                print("Tente outras palavras ou navegue pelas categorias.")

    def navegar(self):
        categorias = self.base.categorias()

        if len(categorias) == 0:
            print("\nA base de conhecimento está vazia.")
            return

        while True:
            print("\n" + "=" * 45)
            print("CATEGORIAS")
            print("=" * 45)

            numero = 1
            for categoria in categorias:
                print(f"{numero} - {categoria}")
                numero += 1
            print("0 - Voltar")

            escolha = self.ler_numero(len(categorias))

            if escolha == 0:
                break

            categoria = categorias[escolha - 1]
            orientacoes = self.base.por_categoria(categoria)

            while True:
                print(f"\n--- {categoria} ---")

                numero = 1
                for orientacao in orientacoes:
                    print(f"{numero} - {orientacao.titulo}")
                    numero += 1
                print("0 - Voltar")

                escolha2 = self.ler_numero(len(orientacoes))

                if escolha2 == 0:
                    break

                orientacao = orientacoes[escolha2 - 1]
                inicio = time.time()
                self.mostrar_orientacao(orientacao)
                ajudou = self.ler_sim_nao("\nEssa orientação respondeu sua dúvida? (s/n): ")
                tempo = round(time.time() - inicio, 1)
                self.registrar("categoria", categoria, orientacao.id, True, ajudou, 1, tempo)

    def indicadores(self):
        total = len(self.historico)

        print("\n" + "=" * 45)
        print("INDICADORES")
        print("=" * 45)

        if total == 0:
            print("Ainda não há atendimentos registrados.")
            return

        encontrados = 0
        ajudados = 0
        soma_tempo = 0
        soma_tentativas = 0
        soma_notas = 0
        qtd_notas = 0
        sem_solucao = []

        for atendimento in self.historico:
            if atendimento.get("encontrou"):
                encontrados += 1

            if atendimento.get("ajudou"):
                ajudados += 1
                soma_tempo += atendimento.get("tempo_segundos", 0)
            else:
                duvida = atendimento.get("pergunta", "")
                if duvida not in sem_solucao:
                    sem_solucao.append(duvida)

            soma_tentativas += atendimento.get("tentativas", 1)

            nota = atendimento.get("nota_facilidade")
            if nota:
                soma_notas += nota
                qtd_notas += 1

        print(f"Atendimentos: {total}")
        print(f"Resposta encontrada: {encontrados / total * 100:.1f}%")
        print(f"Taxa de acerto (ajudou): {ajudados / total * 100:.1f}%")

        if ajudados > 0:
            print(f"Tempo médio para encontrar: {soma_tempo / ajudados:.1f} s")
        else:
            print("Tempo médio para encontrar: sem atendimentos resolvidos")

        print(f"Tentativas por atendimento: {soma_tentativas / total:.1f}")

        if qtd_notas > 0:
            print(f"Facilidade de uso (1 a 5): {soma_notas / qtd_notas:.1f}")
        else:
            print("Facilidade de uso (1 a 5): sem notas ainda")

        print("\nDúvidas sem solução:")
        if len(sem_solucao) == 0:
            print("- nenhuma")
        else:
            for duvida in sem_solucao:
                print(f"- {duvida}")

    def exportar_csv(self):
        campos = ["data", "origem", "pergunta", "id_orientacao", "encontrou",
                  "ajudou", "tentativas", "tempo_segundos", "nota_facilidade"]
        try:
            with open("data/atendimentos.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
                escritor = csv.DictWriter(arquivo, fieldnames=campos)
                escritor.writeheader()
                for atendimento in self.historico:
                    escritor.writerow(atendimento)
            print("\nAtendimentos exportados para data/atendimentos.csv")
        except OSError:
            print("\nNão foi possível exportar. Se o CSV estiver aberto, feche e tente de novo.")

    def menu(self):
        while True:
            print("\n" + "=" * 45)
            print("MENU PRINCIPAL")
            print("=" * 45)
            print("1 - Fazer uma pergunta")
            print("2 - Navegar por categorias")
            print("3 - Ver indicadores")
            print("4 - Exportar atendimentos para CSV")
            print("0 - Sair")

            opcao = self.ler_numero(4)

            if opcao == 1:
                self.perguntar()
            elif opcao == 2:
                self.navegar()
            elif opcao == 3:
                self.indicadores()
            elif opcao == 4:
                self.exportar_csv()
            else:
                self.encerrar()
                break

    def encerrar(self):
        if len(self.historico) > self.inicio_sessao:
            print("\nAntes de sair, de 1 a 5, quão fácil foi usar o assistente?")
            nota = self.ler_nota()

            for atendimento in self.historico[self.inicio_sessao:]:
                atendimento["nota_facilidade"] = nota

            self.salvar_historico()

        self.indicadores()
        self.exportar_csv()
        print("\nAté logo!")