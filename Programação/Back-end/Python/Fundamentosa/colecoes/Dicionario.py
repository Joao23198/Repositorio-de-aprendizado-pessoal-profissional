"Dicionários em Python"

"1 - Criação de Dicionários"
pessoa = {"nome": "João", "Idade": 21, "cidade": "Campinas"}

"Cada item é formado por uma chave e um valor"
"As chaves devem ser únicas"

"2 - Acesso a valores"
print(pessoa["nome"])      #João
print(pessoa.get("idade")) #25
".get() evita erro caso não exista a chave"

"3 - Modificação"
pessoa ["idade"] = 26        #Atualiza valor
pessoa ["profissão"] = "Dev" #Adiciona nova chave

"4 - Remoção"
pessoa.pop("cidade") #Remova chave específica
del pessoa("nome")   #outra forma de reomver

"5 - Percorrendo dicionário"
for chave, valor in pessoa.items():
    print(chave, ":", valor)

"6 - Métodos úteis"

print(pessoa.keys())   # Retorna todas as chaves 
print(pessoa.values()) # Retorna todos os valores
print(pessoa.items())  # Retorna pares chave:valor

"7 - Exemplo prático"
estoque = {"maçã": 3, "banana": 5, "Abacate": 7}
for fruta, quantidade in estoque.items():
    print(f"{fruta} : {quantidade} unidades")

"Dicionários são coleções mutáveis que armazenam dados em pares chave:valor"
"São ideais para representar objetos, registros e dados estruturados"
