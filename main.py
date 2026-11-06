print("=============================================")
print("NextJovem - Sistema de Gestão de Jovens")
print("=============================================")

print("\nseja bem vindo ao sistema de gestão de jovens!")
print("\nseu assistente virtual está pronto para te ajudar.")
print("\nO que eu posso fazer por você hoje?")



from base_conhecimento import BaseConhecimento
from assistente import Assistente

base = BaseConhecimento("data/base_conhecimento.json")

base.carregar()

assistente = Assistente("Alfred", base)

assistente.menu()
