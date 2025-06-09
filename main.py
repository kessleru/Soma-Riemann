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

escolha = input("Escolha se deseja usar o limite fornecido ou o valor de m e n (l/mn): ").strip().lower()

if escolha == 'l':
    limite_max = int(input("Digite o limite máximo para n = m: "))
    print(f"Calculando soma de Riemann para diferentes valores de n = m (de 1 até {limite_max}):")
    for limite in range(2, limite_max + 1, 2):
        deltaX = (x2 - x1) / limite
        deltaY = (y2 - y1) / limite
        deltaA = deltaX * deltaY
        matriz = np.zeros((limite, limite))
        
        for i in range(limite):
            for j in range(limite):
                x_val = x1 + (j + 1) * deltaX
                y_val = y1 + (i + 1) * deltaY
                matriz[i, j] = float(fz.subs([(x, x_val), (y, y_val)]) * deltaA)
        
       
        soma_riemann = np.sum(matriz)
        print(f"n = m = {limite} resulta em {soma_riemann:.4f}")

elif escolha == 'mn':
    m = int(input("Digite m (divisões em x): "))
    n = int(input("Digite n (divisões em y): "))
    deltaX = (x2 - x1) / m
    deltaY = (y2 - y1) / n
    deltaA = deltaX * deltaY
    matriz = np.zeros((n, m))
    print(f"Matriz criada com dimensões {n}x{m}")
    print(f"Forma da matriz: {matriz.shape}")
    
    for i in range(n):
        for j in range(m): 
            x_val = x1 + (j + 1) * deltaX
            y_val = y1 + (i + 1) * deltaY
            matriz[i, j] = float(fz.subs([(x, x_val), (y, y_val)]) * deltaA)

    soma_riemann = np.sum(matriz)
    print(f"Usando m = {m} e n = {n} conforme fornecido pelo usuário o que resulta em {soma_riemann}")
    print(f"Soma de Riemann final: {soma_riemann}")

else:
    print("Escolha inválida! Digite 'limite' ou 'mn'.")