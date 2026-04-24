def calcular_dias_passados():
    try:
        dia = int(input("Digite o dia atual (1-30): ")) 
        mes = int(input("Digite o mes atual (1-12): ")) 

        dias_passados = (mes - 1) * 30 + dia
        
        print(f"Desde o início do ano, se passaram {dias_passados} dias.")
        
    except ValueError:
        print("Erro: Por favor, insira números inteiros válidos.")

if __name__ == "__main__":
    calcular_dias_passados()