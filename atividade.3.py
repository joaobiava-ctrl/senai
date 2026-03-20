quant_paes = float (input("digite a quantidade de paes vendidos: "))
quant_broas = float (input("digite a quantidade de broas vendidas: "))  

arecadação = (quant_paes* 0.12) + (quant_broas * 1.50)
poupança = (arecadação * 0.10)

print("total de paes e broas foi: ",arecadação)
print("total de grana na poupança: ",poupança)

