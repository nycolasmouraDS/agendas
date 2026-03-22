#Entrada de dados
nome_do_aparelho = input(('Nome do aparelho:'))
potencia_do_aparelho = int(input('Potência em watts:'))
tempo_medio = int(input('Uso diário em horas:'))

#Processamento
consumo_mensal = potencia_do_aparelho * tempo_medio * 30 / 1000

#Saída
print(f'O ítem {nome_do_aparelho} tem {potencia_do_aparelho}watts de potência')
print(f'De acordo com seu uso diário de {tempo_medio}h o custo mensal é {consumo_mensal}reais por esse elêtronico')
