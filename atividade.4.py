nome =  (input("digite seu nome: "))
idade = float (input("digite sua idade: "))  

if idade > 120 or idade < 0:
    print = ("idade invalida! tente novamente com um valor menor ou igual a  120.")
else: 
    dias_de_vida = idade * 365
    print(f"olá {nome}, voce já viveu cerca de : {dias_de_vida}")



