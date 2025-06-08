from flask import Flask, render_template, request
from sympy import symbols, sympify
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo

app = Flask(__name__)

def calculate_riemann_sum(function_str, x1, x2, y1, y2, m, n):
    """Calcula a soma de Riemann simples"""
    x, y = symbols('x y')
    fz = sympify(function_str)
    
    deltaX = (x2 - x1) / m
    deltaY = (y2 - y1) / n
      # Criar pontos para visualização da função (mais pontos para suavizar)
    x_vals = np.linspace(x1, x2, 50)
    y_vals = np.linspace(y1, y2, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = np.zeros_like(X)
    
    # Calcular função contínua
    for i in range(len(y_vals)):
        for j in range(len(x_vals)):
            Z[i, j] = float(fz.subs([(x, X[i, j]), (y, Y[i, j])]))
      # Calcular pontos de Riemann
    x_riemann, y_riemann, z_riemann = [], [], []
    soma_total = 0
    
    for i in range(n):
        for j in range(m):
            x_val = x1 + (j + 1) * deltaX
            y_val = y1 + (i + 1) * deltaY
            z_val = float(fz.subs([(x, x_val), (y, y_val)]))
            
            x_riemann.append(x_val)
            y_riemann.append(y_val)
            z_riemann.append(z_val)
            soma_total += z_val * deltaX * deltaY
    
    return X, Y, Z, x_riemann, y_riemann, z_riemann, soma_total

@app.route('/')
def index():
    # Obter parâmetros da URL se existirem
    function = request.args.get('function', 'x**2 + y**2')
    x1 = request.args.get('x1', '-2')
    x2 = request.args.get('x2', '2')
    y1 = request.args.get('y1', '-2')
    y2 = request.args.get('y2', '2')
    m = request.args.get('m', '10')
    n = request.args.get('n', '10')
    
    return render_template('index.html', 
                         function=function, x1=x1, x2=x2, 
                         y1=y1, y2=y2, m=m, n=n)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Obter dados do formulário
    function_str = request.form['function']
    x1 = float(request.form['x1'])
    x2 = float(request.form['x2'])
    y1 = float(request.form['y1'])
    y2 = float(request.form['y2'])
    m = int(request.form['m'])
    n = int(request.form['n'])
    
    # Calcular Riemann
    X, Y, Z, x_riemann, y_riemann, z_riemann, soma_total = calculate_riemann_sum(
        function_str, x1, x2, y1, y2, m, n
    )
      # Criar gráfico 3D
    fig = go.Figure()    # Superfície da função
    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        name='Função f(x,y)',
        opacity=0.5,
        colorscale='Viridis',
        showscale=True,
        contours=dict(
            x=dict(show=False),
            y=dict(show=False),
            z=dict(show=False)
        ),
        lighting=dict(
            ambient=0.9,
            diffuse=0.7,
            specular=0.1
        ),
        lightposition=dict(
            x=100,
            y=200,
            z=0
        ),
        hovertemplate='<b>Função Contínua</b><br>' +
                     'x: %{x:.3f}<br>' +
                     'y: %{y:.3f}<br>' +
                     'f(x,y): %{z:.3f}<br>' +
                     '<extra></extra>',
        hoverlabel=dict(
            bgcolor='blue',
            bordercolor='white',
            font=dict(color='white', size=12)
        ),
        hoverinfo='text',
        surfacecolor=Z,
        hidesurface=False
    ))# Pontos de Riemann
    fig.add_trace(go.Scatter3d(
        x=x_riemann, y=y_riemann, z=z_riemann,
        mode='markers',
        name='Pontos Riemann',
        marker=dict(
            size=9,
            color='#FF0000',
            opacity=1.0,
            line=dict(
                color='#FFFFFF',
                width=2
            ),
            symbol='circle'
        ),
        hovertemplate='<b>Ponto Riemann</b><br>' +
                     'x: %{x:.3f}<br>' +
                     'y: %{y:.3f}<br>' +
                     'f(x,y): %{z:.3f}<br>' +
                     '<extra></extra>',
        hoverlabel=dict(
            bgcolor='red',
            bordercolor='white',
            font=dict(color='white', size=12)
        ),
        hoverinfo='text'
    ))    # Layout melhorado
    fig.update_layout(
        title=dict(
            text=f'Soma de Riemann = {soma_total:.6f}',
            x=0.5,
            font=dict(size=18, color='darkblue')
        ),
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y', 
            zaxis_title='f(x,y)',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            ),
            aspectmode='cube',
            xaxis=dict(
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                showline=False,
                zeroline=False
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                showline=False,
                zeroline=False
            ),
            zaxis=dict(
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                showline=False,
                zeroline=False
            )
        ),
        width=1000,
        height=800,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=0.01,
            font=dict(size=14)
        ),
        margin=dict(l=0, r=0, b=0, t=50),
        hovermode='closest'
    )
    
    # Gerar HTML do gráfico
    graph_html = pyo.plot(fig, output_type='div', include_plotlyjs=True)
    
    return render_template('result.html', 
                         graph_html=graph_html, 
                         soma=soma_total,
                         function=function_str,
                         x1=x1, x2=x2, y1=y1, y2=y2, m=m, n=n)

if __name__ == '__main__':
    app.run(debug=True)
