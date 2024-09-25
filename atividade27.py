# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria

convidados = []

for i in range(1, 8):

    nome = input(f"digite o nome do convidado {i}:")
    convidados.append(nome)

remover = input("voce deseja remover algum convidado da lista? (sim/não): ")

if remover == "sim":
    nome_remover = input("digite o nome de quem você quer remover: ")
    if nome_remover in convidados:
        convidados.remove (nome_remover)
        print (f"{nome_remover} foi removido da lista.")
    else:
        print (f"{nome_remover} não esta na lista")

#exibe a lista final dos convidados

print ("lista final de convidados")

for convidados in convidados:
  print (convidados)



    
    





