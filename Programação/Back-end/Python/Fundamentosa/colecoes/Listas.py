"Listas em Python!"

"1 - Criação de listas"

frutas = ["maçã", "pêra", "ameixa", "pêssego"]
numeros = [1,2,3,4,5]
razão = [True or False]
mistureba = ["Banana", 1,2,3, True, "Manga", False, 4,5 ]

"Podem armazenar uma série de diferentes tipos de dados."
"São estruturas mutáveis, podem ser editadas."

"2 - Acesso por índice"

print(frutas[0]) # maçã
print(frutas[-1]) # Pêssego (último elemento)

"Índices começam em zero."
"Índices negativos, começam de trás pra frente"

"3 - Operação Básicas"
frutas.append("laranja") # adiciona no fim
frutas.insert(1, "pera") # adiciona na posição
frutas.remove("banana")  # remove pelo valor
frutas.pop()             # remove o último
print(len (frutas))      # tamanha

"4 - Percorrendo listas"

for fruta in frutas:
    print(fruta)

"5 - Fatiamento"

numeros = [0,1,2,3,4,5]

print(numeros[1:4]) # [1, 2, 3]
print(numeros[:3])  # [0, 1, 2]
print(numeros[::2]) # [0, 2, 4]

"6 - List Comprehension."

quadrados = [x**2 for x in range (6)]
print(quadrados) # [0, 1, 4, 9, 16, 25]

"7 - Funções úteis"

numeros = [3, 1, 4, 2]
print(max(numeros)) # 4
print(min(numeros)) # 1
print(sum(numeros)) # 10
numeros.sort()      # ordena
