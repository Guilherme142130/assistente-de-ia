print("=============================================")
print("Alfred Jovem - Assistente Virtual")
print("=============================================")
 
print("\nseja bem vindo ao sistema de gestão de jovens!")
print("\nseu assistente virtual está pronto para te ajudar.")
print("\nO que eu posso fazer por você hoje?")
 
 
 
from pathlib import Path
 
from base_conhecimento import BaseConhecimento
from assistente import Assistente
 
pasta_projeto = Path(__file__).resolve().parent
base = BaseConhecimento(pasta_projeto / "data" / "base_conhecimento.json")
 
base.carregar()
 
assistente = Assistente("Alfred", base)
 
assistente.menu()