"if" = "Executa um bloco de código se a condicao inserida for verdadeira"

idade = 18

if idade >= 18:
    print("Maior de idade")

"If/Else" = "Permite escolher entre dois caminhos"

idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

"If/Else/Elif" = "Permite escolher entre multiplas opções "

nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Reprovado")

"Condicionais Aninhadas" = "Um if dentro de outro"

idade = 20
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Pode Dirigir")
    else:
        print("precisa de carteira")
else:
    print("Menor de Idade")

"Operadores Lógicos em Condicoes" = "Usados para combinar condições"

idade = 20
tem_carteira = False

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
else:
    print("Não pode dirigir")












