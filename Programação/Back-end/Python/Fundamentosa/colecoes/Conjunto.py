"Conjuntos em Python"

"1 - Criação de Conjuntos"

numeros = {1,2,3,4,5}
print(numeros)       # {1,2,3,4,5}

"Não permitem elementos repetidos"
"Não possuem ordem fixa"

"2 - Adição e remoção"
numeros = {1,2,3}

numeros.add(4)    #adiciona
numeros.remove(2) #remove
print(numeros)    #{1,3,4}

"3 - Operações Matemáticas"

A = {1,2,3}
B = {3,4,5}

print(A.difference(B))   # diferença = {1, 2}
print(A.intersection(B)) # intersecção = {3}
print(A.union(B))        # união = {1,2,3,4,5}

"4 - Verificação de associação"

numeros = {1,2,3}
print(2 in numeros)     # True
print(5 not in numeros) # True

"5 - Exemplo prático"

"Remover duplicados de uma lista"

lista = {1,2,2,3,3,4,5}
sem_repetidos = set(lista)
print(sem_repetidos)
