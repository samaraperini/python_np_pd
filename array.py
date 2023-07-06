import numpy as np

#criando array (0,1,2,3,4,5,6,7,8)
x = np.arange(0, 9)

print("x:\n", x)

#reshape: transformar a matriz em um vetor coluna
print("rashape de x:\n", x.reshape(9,1))

#reshape para 3 linhas e 3 colunas
x = x.reshape(3,3)

#trasnposição de matriz: de coluna para linha ou linha para coluna
print("transposição de x:\n",x.T)

#np.sum: soma em um dado eixo, axis = (0:linha, 1:coluna)
print("x np.sum todos elementos:\n", np.sum(x))
print("soma de x ao longo das linhas:\n", np.sum(x, axis=0))
print("soma de x ao longo das colunas:\n", np.sum(x, axis=1))

#np.mean: média em um dado eixo, axis = (0:linha, 1:coluna)
print("x np.mean todos elementos:\n", np.mean(x))
print("média de x ao longo das linhas:\n", np.mean(x, axis=0))
print("média de x ao longo das colunas:\n", np.mean(x, axis=1))

#np.where: identificação dos índices onde uma dada condição é atendida. Usd conjunto com indexação bolenana
cond = x % 2 == 0 #numeros pares
print("condição:\n", cond)
i,j = np.where(cond)
#localização de onde a condição é verdadeira (linha, coluna)
print("índice i (linhas):", i)
print("índice j (colunas):", j)

#indexação boleana e slicing: selecionar as linhas de x que têm números pares
#se houver True na linha a soma sera > 0
i_row = np.where(np.sum(cond,axis=1))[0]
print("índice nas linhas que possuem números pares:", i_row)
print("linhas que possuem números pares:\n", x[i_row,:])

