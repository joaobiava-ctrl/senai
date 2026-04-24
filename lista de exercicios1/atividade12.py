
salario_inicial = float(input("Digite o salário inicial: "))


salario_aumento = salario_inicial * 1.15


salario_final = salario_aumento * 0.92

print(f"Salário Inicial: R${salario_inicial:.2f}")
print(f"Salário com Aumento: R${salario_aumento:.2f}")
print(f"Salário Final (após impostos): R${salario_final:.2f}")