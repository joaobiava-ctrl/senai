

dias_totais = int(input("Digite a quantidade de dias sem acidentes: "))

anos = dias_totais // 360
resto_anos = dias_totais % 360

meses = resto_anos // 30
dias = resto_anos % 30

print(f"Tempo sem acidentes: {anos} anos, {meses} meses e {dias} dias.")