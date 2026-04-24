quantidade = int(input("Digite a quantidade de sanduíches a fazer: "))


peso_queijo = (quantidade * 100) / 1000
peso_presunto = (quantidade * 50) / 1000
peso_hamburguer = (quantidade * 100) / 1000

print(f"Para {quantidade} sanduíches você precisará de:")
print(f"{peso_queijo:.2f} kg de queijo")
print(f"{peso_presunto:.2f} kg de presunto")
print(f"{peso_hamburguer:.2f} kg de carne de hambúrguer")