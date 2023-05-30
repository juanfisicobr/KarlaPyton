import numpy as np
import matplotlib.pyplot as plt

def loop_inflation_potential(X, alpha):
    M = 1.0  # Valor para M 
    return M**4 * (1 + alpha * np.log(X))

# Parâmetros
alpha = 0.5  # Valor para alpha 

# Dados para o gráfico
X_vals = np.linspace(0.1, 10, 100)  # Intervalo de valores para X
V_vals = loop_inflation_potential(X_vals, alpha)

# Plotagem do gráfico
plt.plot(X_vals, V_vals, label='Loop Inflation Potential')

# Configurações do gráfico
plt.xlabel('X')
plt.ylabel('V')
plt.title('Loop Inflation - One Parameter Models')
plt.legend()

# Salvar o gráfico como uma imagem
plt.savefig('loop_inflation_plot.png')

# Exibindo o gráfico
plt.show()
