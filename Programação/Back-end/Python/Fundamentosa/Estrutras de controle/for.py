"Laço For em Python"

"1 - Percorrendo listas"

frutas = ["manga", "baana", "uva"]

for fruta in frutas:
    print (fruta)

"2 - Usando Range()"
"O Range() gera uma sequência de números"

for i in range(5):
    print(i)

"3 - Enumerate"
"Permite acessar índice e valor ao mesmo tempo"

frutas = ["maçã", "ameixa", "pêra"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)

"4 - For com dicionário"

pessoa = {"nome": "João", "idade":25}

for chave, valor in pessoa.items():
    print(chave, ":", valor)

"5 - Compreensão de listas"
"Forma compacta de criar listas usando for"

quadrados = [x**2 for x in range ()]
print(quadrados)

