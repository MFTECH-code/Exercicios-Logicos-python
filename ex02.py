# Sistema de opções
print("NNC compania de viagens")
print("Qual a região do destino:")
print("""1 - Norte
2 - Nordeste
3 - Centro-Oeste""")
destino = int(input("Digite sua opção: "))
# Validação da opção
if (destino < 1 or destino > 3):
    print("Opção inválida...")
    print("Fim do programa")
else:
    print("Somente ida ou ida e volta:")
    print("""1 - Somente ida
2 - Ida e volta""")
    tipo_viagem = int(input("Digite sua opção: "))
    # Validação da opção
    if (tipo_viagem < 1 or tipo_viagem > 2):
        print("Opção inválida...")
        print("Fim do programa")
    else:
        if (destino == 1 and tipo_viagem == 1):
            preco_viagem = 280
            print(f'O valor da passagem é R${preco_viagem},00')
        elif (destino == 1 and tipo_viagem == 2):
            preco_viagem = 400
            print(f'O valor da passagem é R${preco_viagem},00')
        elif (destino == 2 and tipo_viagem == 1):
            preco_viagem = 380
            print(f'O valor da passagem é R${preco_viagem},00')
        elif (destino == 2 and tipo_viagem == 2):
            preco_viagem = 628
            print(f'O valor da passagem é R${preco_viagem},00')
        elif (destino == 3 and tipo_viagem == 1):
            preco_viagem = 620
            print(f'O valor da passagem é R${preco_viagem},00')
        elif (destino == 3 and tipo_viagem == 2):
            preco_viagem = 1100
            print(f'O valor da passagem é R${preco_viagem},00')
        print("Fim do programa...")