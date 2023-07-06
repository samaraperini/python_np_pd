import numpy as np

# criação de um array 1D: [1, 2, 3]
l = [1, 2, 3]
x = np.array(l)
print("x:", x)
print("shape:", x.shape)

# criação de um array 2D: listas aninhadas
l = [[1, 2], [3, 4]]
x = np.array(l)
print("x:\n", x)
print("shape:", x.shape)

# array contendo apenas 0's
dim = (2, 2)  # (linhas, colunas)
x = np.zeros(dim)
print("x:\n", x)
print("shape:", x.shape)

# array contendo apenas 1's
size = (2, 2)  # (linhas, colunas)
x = np.ones(size)
print("x:\n", x)
print("shape:", x.shape)

# criação de valores dentro de um intervalo
# valores uniformes entre 5 e 15
x_min, x_max = 5, 15
x = np.linspace(start=x_min, stop=x_max, num=6)
print("x:", x)
print("shape:", x.shape)

# criação da matriz identidade
n = 4
x = np.eye(n)
print("x:\n", x)
print("shape:", x.shape)

# criação de valores aleatórios
# np.random.seed(10)
x = np.random.random(size=(2, 3))
print("x:\n", x)
print("shape:", x.shape)

# os índices no Python vão de 0 a n-1,
# onde n é o tamanho da dimensão
x = np.linspace(start=10, stop=100, num=10)
print("x:", x)
print("shape:", x.shape)

# extração de elementos
print("x:", x)
print("primeiro elemento:", x[0])
print("segundo elemento:", x[1])
print("último elemento:", x[9])
print("último elemento:", x[-1])

# slicing: extração de subarrays:
print("x:", x)
print("dois primeiros elementos:", x[0:2])  # 2 é exclusivo
print("dois primeiros elementos:", x[:2])
print("dois últimos elementos:", x[-2:])

# slicing em arrays 2D (matrizes)
x = x.reshape(2, 5)  # reshape de x para 2 linhas e 5 colunas
print("x:\n", x)

# extração de elementos
print("primeira linha, segunda coluna:", x[0, 1])
print("segunda linha, penúltima coluna:", x[1, -2])
print("última linha, última coluna:", x[1, 4])
print("última linha, última coluna:", x[-1, -1])

# slicing: extração de subarrays
print("x:\n", x)
print("primeira linha inteira: ", x[0, :])
print("primeira linha, segunda a quarta coluna: ", x[0, 1:4])
print("última coluna inteira:\n", x[:, [-1]])

# atenção com compartilhamento de memória em subarrays!!
x = np.array([1, 2, 3])
print("x antes:", x)
y = x[:2]
y[0] = -100  # alteração do valor em y altera o valor de x
print("x depois:", x)

# atenção com compartilhamento de memória em subarrays!!
x = np.array([1, 2, 3])
print("x antes:", x)
y = x[:2].copy()
y[0] = -100  # alteração do valor em y altera o valor de x
print("x depois:", x)

# criação de dois arrays x e y
x = np.ones((2, 2))
y = np.eye(2)
print("x: \n", x)
print("y: \n", y)

# soma
print("soma de dois arrays:\n", x + y)
print("soma com float/int:\n", x + 2.)  # broadcasting

# subtração
print("subtração de dois arrays:\n", x - y)
print("subtração com float/int:\n", x - 2)  # broadcasting

# divisão
print("divisão de dois arrays:\n", x / y)
print("divisão com float/int:\n", x / 2)  # broadcasting

# soma, subtração e divisão
print("combinação de operações: \n", (x+y)/(x-2))

# quando o broadcasting não funciona
# np.array([1, 2, 3]) + np.array([1, 2])

# multiplicação
print("multiplicação de dois arrays:\n", x * y)
print("multiplicação com float/int:\n", x * 2)  # broadcasting

# multiplicação matricial
print("multiplicação matricial (np.dot):\n", np.dot(x, y))
print("multiplicação matricial (@):\n", x @ y)
print("multiplicação matricial (.dot):\n", x.dot(y))

# comparações ponto a ponto
print("Comparação de um array com um escalar (>): \n", x > 2)
print("Comparação de um array com um escalar (>=): \n", x >= 2)
print("Comparação de um array com um escalar (<): \n", x < 2)
print("Comparação de um array com um escalar (<=): \n", x <= 2)
print("Comparação entre arrays (==): \n", x == x)
print("Comparação entre arrays (>): \n", x > x)
print("Comparação entre arrays (>): \n", x > y)  # broadcasting