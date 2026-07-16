"While"
"1 - Estrutura básica"

contador = 0

while contador <5:
    print("Contador:", contador)
    contador += 1

"2 - Loop infinito"

while True:
    print("isso nunca acaba")

"3 - Controle de fluxo"

contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    if contador == 8:
        break
    print(contador)
"4 - Exemplo prático"

senha = ""

while senha != "1234":
    senha = input("Digite a senha")
print("Acesso permitido")