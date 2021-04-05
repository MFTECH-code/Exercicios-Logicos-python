salario = float(input("Digite o valor do seu salário bruto: R$"))
if (salario > 0):
    limite = salario * 0.3
    print(f"Limite da prestação: R${limite}")
    emprestimo = float(input("Digite o valor do empréstimo: R$"))
    if (emprestimo > 0):
        # O valor do empréstimo não pode passar de 30% do valor do salário 
        if salario * 0.3 >= emprestimo:
            print("Empréstimo aceito com sucesso!")
        else:
            print("Empréstimo negado! Salário incompatível...")
    else:
        print("Valor da prestação inválido...")
else:
    print("Valor do salário inválido")