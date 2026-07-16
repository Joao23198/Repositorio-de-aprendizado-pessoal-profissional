"Funções em python"

"1 - Definição"

"Criado com a palavra chave def"

def saudacao():
    print("ola mundo")

saudacao()

"2 - Parâmetros"

"Permitem passar valores para dentro da função "

def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("Joao")

"3 - Retorno"

"Use return para devolver valores "

def soma(a,b):
    return a + b

    resultado = soma(3,5)
    print(resultado) #8

"4 - Parâmetros padrão"

def saudacao(nome="Visitante"):
    print(f"Olá, {nome} ")

saudacao()
saudacao("joão")

"5 - Funções anônimas"

"Funções pequenas em uma única linha"

quadrado = lambda x: x**2
print(quadrado(4))


"6 - Escopo de variáveis"

Local = "Dentro da função"
Global = "Fora da função"

x = 10

def mostrar (x):
    x = 5
    print(x)
mostrar()
print(x)

"7 - Recursão"

def fatorial (n):
    if n == 0:
        return 1
    return n * fatorial(n-1)
print(fatorial(5)) #120

"Uma função que chama a si mesma"