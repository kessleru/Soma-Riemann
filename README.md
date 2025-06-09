# 📊 Soma de Riemann - Visualização 3D

Um projeto interativo para calcular e visualizar Somas de Riemann de funções de duas variáveis com interface web 3D.

## 📝 Sobre o Projeto

Este projeto possui duas interfaces:
- **Interface Web (`app.py`)**: Desenvolvida com Flask, Plotly e Bootstrap para visualização 3D interativa. *Interface criada com auxílio do Claude Sonnet 4.*
- **Interface Terminal (`main.py`)**: Código original que funciona via linha de comando.

### 🌿 Branches Disponíveis

- **`main`**: Versão completa com interface web e terminal
- **`Terminal`**: Branch contendo apenas o código original de linha de comando (`main.py`)

## 🚀 Funcionalidades

- **Interface Web Interativa**: Interface moderna e responsiva usando Flask e Bootstrap
- **Visualização 3D**: Gráficos 3D interativos usando Plotly para melhor compreensão
- **Cálculo Preciso**: Implementação matemática usando SymPy e NumPy
- **Interface CLI**: Versão em linha de comando para uso rápido
- **Suporte a Funções Personalizadas**: Digite qualquer função matemática de duas variáveis

## 🛠️ Tecnologias Utilizadas

### Interface Web (`app.py`)
- **Python 3.x**
- **Flask** - Framework web
- **Plotly** - Visualizações 3D interativas
- **Bootstrap 5** - Interface responsiva
- *Desenvolvida com auxílio do Claude Sonnet 4*

### Core Matemático (ambas as interfaces)
- **SymPy** - Computação simbólica
- **NumPy** - Computação numérica

### Interface Terminal (`main.py`)
- **Python 3.x** 
- **SymPy e NumPy** - Código original para cálculos de Riemann

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Soma-Riemann.git
cd Soma-Riemann
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🎯 Como Usar

### Interface Web (Recomendado)

1. Execute a aplicação Flask:
```bash
python app.py
```

2. Abra seu navegador e acesse: `http://localhost:5000`

3. Preencha os campos:
   - **Função f(x,y)**: Digite sua função (ex: `x**2 + y**2`, `sin(x)*cos(y)`)
   - **Limites de integração**: Defina os intervalos [x1, x2] e [y1, y2]
   - **Divisões**: Escolha o número de subdivisões (m para x, n para y)

4. Clique em "Calcular" para visualizar o resultado em 3D

### Interface CLI (Código Original)

Para usar apenas o código original sem interface web, você pode alternar para o branch `Terminal`:

```bash
git checkout Terminal
```

Ou execute o `main.py` no branch atual:

```bash
python main.py
```

Siga as instruções no terminal para inserir:
   - Função f(x,y)
   - Limites de integração
   - Número de divisões


## 🧮 Como Funciona

A **Soma de Riemann** é uma aproximação numérica para integrais duplas:

```
∬f(x,y) dA ≈ Σ Σ f(xᵢ,yⱼ) * ΔA
```

Onde:
- `ΔA = Δx * Δy` é a área de cada retângulo
- `Δx = (b-a)/m` e `Δy = (d-c)/n`
- `(xᵢ,yⱼ)` são os pontos de avaliação

## 🎨 Capturas de Tela

A interface web oferece:
- Formulário intuitivo para entrada de dados
- Visualização 3D interativa da função
- Pontos de Riemann destacados
- Resultado numérico da soma

### Desenvolvimento
- **Código Original (`main.py`)**: Implementação matemática base para cálculo de Somas de Riemann via terminal
- **Interface Web (`app.py`)**: Desenvolvida com auxílio do **Claude Sonnet 4** para criar a interface Flask com visualização 3D interativa

### Estrutura do Projeto
- **Branch `main`**: Versão completa com ambas as interfaces
- **Branch `Terminal`**: Apenas o código original de linha de comando

Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades!

## 🔗 Recursos Úteis

- [Documentação SymPy](https://docs.sympy.org/)
- [Documentação NumPy](https://numpy.org/doc/)
- [Documentação Flask](https://flask.palletsprojects.com/)
- [Documentação Plotly](https://plotly.com/python/)
- [Integrais Duplas - Wikipedia](https://pt.wikipedia.org/wiki/Integral_dupla)

