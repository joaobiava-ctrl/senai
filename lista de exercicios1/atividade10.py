
x1 = float(input("x do primeiro ponto: "))
y1 = float(input("y do primeiro ponto: "))
x2 = float(input("x do segundo ponto: "))
y2 = float(input("y do segundo ponto: "))

diferença_x = x2 - x2
diferença_y = y2 - y1
          
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"A distância entre os pontos é: {distancia:.2f}")