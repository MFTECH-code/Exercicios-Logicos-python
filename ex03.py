numero = int(input("Digite o número de 3 digitos: "))
# Separação dos digitos
resto1 = numero % 100 # Resto que acha os ultimos 2 digitos
primeiro_digito = numero // 100 # Primeiro digito da centena
segundo_digito = resto1 // 10 # Segundo digito
terceiro_digito = resto1 % 10 # Terceiro digito

# Pegar o inverso e somar com o número normal
numero_inverso = terceiro_digito * 100 + segundo_digito * 10 + primeiro_digito
soma = numero + numero_inverso
# Separação dos digitos
resto2 = soma % 100
soma_primeiro_digito = soma // 100
soma_segundo_digito = resto2 // 10
soma_terceiro_digito = resto2 % 10

soma2 = soma_primeiro_digito * 1 + soma_segundo_digito * 2 + soma_terceiro_digito * 3
# Pegando codigo verificador
cod_verificador = soma2 % 10
print(f'{numero}-{cod_verificador}')

