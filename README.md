# 📊 Soma de Riemann - Visualização 3D

Um projeto interativo para calcular e visualizar Somas de Riemann de funções de duas variáveis com interface web 3D.

## 🚀 Funcionalidades

- **Interface Web Interativa**: Interface moderna e responsiva usando Flask e Bootstrap
- **Visualização 3D**: Gráficos 3D interativos usando Plotly para melhor compreensão
- **Cálculo Preciso**: Implementação matemática usando SymPy e NumPy
- **Interface CLI**: Versão em linha de comando para uso rápido
- **Suporte a Funções Personalizadas**: Digite qualquer função matemática de duas variáveis

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **SymPy** - Computação simbólica
- **NumPy** - Computação numérica
- **Plotly** - Visualizações 3D interativas
- **Bootstrap 5** - Interface responsiva

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

### Interface CLI

1. Execute o script principal:
```bash
python main.py
```

2. Siga as instruções no terminal para inserir:
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

