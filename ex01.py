salario = float(input("Digite o valor do seu salário bruto: R$"))
emprestimo = float(input("Digite o valor do empréstimo: R$"))

# O valor do empréstimo não pode passar de 30% do valor do salário 

if salario * 0.3 >= emprestimo:
    print("Empréstimo aceito com sucesso!")
else:
    print("Empréstimo negado! Salário incompatível...")