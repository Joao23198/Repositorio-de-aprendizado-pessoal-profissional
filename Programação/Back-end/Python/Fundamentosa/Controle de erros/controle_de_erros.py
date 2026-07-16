"Tratamento de erros"

"1 - Bloco try/except"

"Permite capturar erros e evitar que o programa quebre"

try:
    numero = int(input("Digite um número:"))
    print(10/numero)
except ValueError:
    print("Voce nao digitou um número válido")
except ZeroDivisionError:
    print("Não é possível dividir por zero")

"2 - Bloco finally"

"Executa sempre, independentemente de erro"

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
finally:
    print("Operação finalizada")

"3 -  Bloco else"

"Executa apenas se nenhum erro acontecer"

try:
    numero = int(input("Digite um número"))
except ValueError:
    print("Entrada inválida")
else:
    print(f"Voce digitou {numero}")

"4 - Exceções personalizadas"

"Podemos criar nossos próprios tipos de erro"

class ErroPersonalizado(Exception):
    pass

def verificar_valor(x):
    if x < 0:
        raise ErroPersonalizado("Valor nao pode ser negativo")
    return x
try:
    verificar_valor(-5)
except ErroPersonalizado as e:
    print(e)
