"Tuplas em Python"

"1 - Criação de Tuplas"

coordenadas = (10,20)
valores = (1,2,3,4)
mistura = ("texto", 42, True or False)

"Usam parênteses () em vez de colchetes"
"São imutáveis: não é possível adicionar, remover ou alterar elementos de uma tupla"

"2 - Acesso por índice"

print(coordenadas[0]) # 10
print(coordenadas[1]) # 20

"Igual as listas, indices começam em zero."

"3 - Tupla de um elemento"

"É necessário usar vírgula para diferenciar de um simples valor"
tupla_unica = (5,)
print(type(tupla_unica)) # <class 'tuple'>

"4 - Desempacotamento"

"Permite atribuir valores diretamente"

ponto = (3, 4)
x, y = ponto
print(x) # 3
print(y) # 4

"5 - Uso comum"

"Representar dados fixos (ex: coordenadas, datas)"
"Garantir que os valores não sejam alterados"
"Retornar múltiplos valores de uma função"

def dividir (a, b):
    quociente = a // b
    resto = a % b
    return(quociente, resto)

resultado = dividir(10, 3)
print(resultado) # (10, 3)

"Diferença principal:"
"Lista >>> mutável, pode ser alterada"
"Tupla >>> imutável, não pode ser alterada"






















































































































