total_conta = float(input("Digite o valor total da conta: "))

valor_inteiro = int(total_conta // 3)

valor_felipe = total_conta - (valor_inteiro * 2)

print(f"Carlos deve pagar: R${valor_inteiro:.2f}")
print(f"André deve pagar: R${valor_inteiro:.2f}")
print(f"Felipe deve pagar: R${valor_felipe:.2f}")