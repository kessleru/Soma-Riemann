from sympy import symbols, sympify
import numpy as np


print("Soma de Riemann")

x, y = symbols('x y')

z = input("Digite a função f(x, y): ")
fz = sympify(z)

x1 = float(input("Digite o valor de x1 (a): "))
x2 = float(input("Digite o valor de x2 (b): "))
y1 = float(input("Digite o valor de y1 (c): "))
y2 = float(input("Digite o valor de y2 (d): "))

m = int(input("Digite m (divisões em x): "))
n = int(input("Digite n (divisões em y): "))

deltaX = (x2 - x1) / m
deltaY = (y2 - y1) / n
deltaA = deltaX * deltaY

matriz = np.zeros((n, m))
print(f"Matriz criada com dimensões {n}x{m}")
print(f"Forma da matriz: {matriz.shape}")


print("Calculando valores da função...")
for i in range(n):
    for j in range(m): 
        x_val = x1 + (j + 1) * deltaX
        y_val = y1 + (i + 1) * deltaY
        matriz[i, j] = float(fz.subs([(x, x_val), (y, y_val)]) * deltaA)
        
# Calculando a soma de Riemann
soma_riemann = np.sum(matriz)
print(f"Soma de Riemann: {soma_riemann}")