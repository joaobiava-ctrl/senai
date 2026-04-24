def calcular_valor_refeicao():
    preco_por_quilo = 12.00

    try:
        peso_prato = float(input("Digite o peso do prato (em kg): "))
        
        valor_pagar = peso_prato * preco_por_quilo
        
        print(f"O valor total a pagar é: R${valor_pagar:.2f}")
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido para o peso.")

if __name__ == "__main__":
    calcular_valor_refeicao()