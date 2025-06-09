# Calculadora de Soma de Riemann para Integrais Duplas

Este projeto implementa uma calculadora de **Soma de Riemann** para aproximar integrais duplas de funções de duas variáveis f(x, y) sobre uma região retangular.

## 📋 Descrição

A Soma de Riemann é um método numérico usado para aproximar integrais definidas. Este programa calcula a integral dupla:

```
∬[a,b]×[c,d] f(x,y) dA
```

Onde:
- `f(x,y)` é uma função de duas variáveis
- `[a,b] × [c,d]` é a região retangular de integração
- `dA = dx dy` é o elemento de área

## 🚀 Funcionalidades

- **Entrada de função simbólica**: Digite funções usando sintaxe matemática (ex: `x**2 + y**2`, `sin(x)*cos(y)`)
- **Dois modos de cálculo**:
  - **Modo Limite (`l`)**: Calcula para diferentes valores de n = m (de 2 até um limite máximo)
  - **Modo Manual (`mn`)**: Permite especificar valores personalizados para m e n divisões
- **Visualização de resultados**: Mostra a aproximação da integral para diferentes precisões

## 📦 Dependências

```bash
pip install sympy numpy
```

## 🔧 Como usar

1. **Execute o programa**:
   ```bash
   python main.py
   ```

2. **Digite a função**: Exemplo: `x**2 + y**2`

3. **Defina os limites de integração**:
   - x1 (a): limite inferior em x
   - x2 (b): limite superior em x
   - y1 (c): limite inferior em y
   - y2 (d): limite superior em y

4. **Escolha o modo**:
   - `l`: Para calcular com diferentes valores de n = m
   - `mn`: Para especificar m e n manualmente

### Exemplo de uso

```
Soma de Riemann
Digite a função f(x, y): x**2 + y**2
Digite o valor de x1 (a): 0
Digite o valor de x2 (b): 1
Digite o valor de y1 (c): 0
Digite o valor de y2 (d): 1
Escolha se deseja usar o limite fornecido ou o valor de m e n (l/mn): l
Digite o limite máximo para n = m: 10

Calculando soma de Riemann para diferentes valores de n = m (de 1 até 10):
n = m = 2 resulta em 0.7500
n = m = 4 resulta em 0.7031
n = m = 6 resulta em 0.6944
n = m = 8 resulta em 0.6914
n = m = 10 resulta em 0.6900
```

## 🧮 Como funciona

### Algoritmo da Soma de Riemann

1. **Divisão da região**: A região retangular [a,b] × [c,d] é dividida em uma grade de m × n retângulos
2. **Cálculo dos deltas**:
   - `Δx = (b - a) / m`
   - `Δy = (d - c) / n`
   - `ΔA = Δx × Δy` (área de cada retângulo)

3. **Avaliação da função**: Para cada retângulo, a função é avaliada no ponto:
   - `x_val = a + (j + 1) × Δx`
   - `y_val = c + (i + 1) × Δy`

4. **Soma**: A integral é aproximada por:
   ```
   ∬ f(x,y) dA ≈ Σ Σ f(x_ij, y_ij) × ΔA
   ```

### Estrutura do código

- **Entrada de dados**: Função simbólica e limites de integração
- **Processamento**: Cálculo da soma de Riemann usando NumPy para eficiência
- **Saída**: Resultados formatados com precisão de 4 casas decimais

## 📚 Conceitos matemáticos

- **Integral dupla**: Integração sobre uma região bidimensional
- **Soma de Riemann**: Método de aproximação numérica
- **Convergência**: À medida que m e n aumentam, a aproximação se torna mais precisa