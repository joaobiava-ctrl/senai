
p = int(input("Quantidade de camisetas Pequenas: "))
m = int(input("Quantidade de camisetas Médias: "))
g = int(input("Quantidade de camisetas Grandes: "))

total = (p * 10) + (m * 12) + (g * 15)

print(f"O valor total arrecadado é: R${total:.2f}")