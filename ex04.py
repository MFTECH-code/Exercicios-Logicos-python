numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

resultado = ((numero_1 % 2) * 3) + (13 - 2 + numero_2)
print(resultado)

if (resultado <= 0):
    print("Resultado menor ou igual a ZERO")
elif (resultado > 0 and resultado <= 20):
    print("O resultado é maior do que ZERO e menor ou igual a 20")
else:
    print("O resultado é maior que 20")