numero = int(input("Digite o número de 3 digitos: "))
# Separação dos digitos
resto1 = numero % 100 # Separando somente a dezena da centena
primeiro_digito = numero // 100 # Pegando o digito da centena
segundo_digito = resto1 // 10 # Pegando o digito da dezena
terceiro_digito = resto1 % 10 # Pegando o digito da unidade
# O resto1 -> é a dezena separada da centena, que usamos para separar para pegar somente os digitos da dezena e da unidade

# Pegar o inverso e somar com o número normal
numero_inverso = terceiro_digito * 100 + segundo_digito * 10 + primeiro_digito
soma = numero + numero_inverso
# Separação dos digitos
if (soma < 1000):
    resto2 = soma % 100
    soma_primeiro_digito = soma // 100
    soma_segundo_digito = resto2 // 10
    soma_terceiro_digito = resto2 % 10
    soma2 = soma_primeiro_digito * 1 + soma_segundo_digito * 2 + soma_terceiro_digito * 3
else:
    resto2 = soma % 1000
    resto3 = resto2 % 100
    soma_primeiro_digito = soma // 1000
    soma_segundo_digito = resto2 // 100 
    soma_terceiro_digito = resto3 // 10
    soma_quarto_digito = resto3 % 10
    soma2 = soma_primeiro_digito * 1 + soma_segundo_digito * 2 + soma_terceiro_digito * 3 + soma_quarto_digito * 4
# Pegando codigo verificador
cod_verificador = soma2 % 10
print(f'{numero}-{cod_verificador}')

