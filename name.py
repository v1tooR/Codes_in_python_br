#name = "vamos la!"
#print(name.title())

#nome = "let's go!"
#print(nome.upper())
#print(nome.lower())

#>>> Salvando dados em variáveis
first_name = "victor"
last_name = "santos"
full_name = first_name+" "+last_name

message = "Hello, " + full_name.title() + "!"

print(message)

languages = "\tphyton\n\tjava\n\tc++"
print("Our courses:\n"+ languages.title())

#>>>Removendo espaços em branco
favorite_language = 'phyton '
favorite_language = favorite_language.rstrip()
print("\n\n",favorite_language)

#.rstrip -> apagar a direita // .lstrip -> apagar a esquerda (o espaço em branco)
#(name_cases.py)2.3

nome = "victor"

message = "Ola ,bem vindo ao curso de Phyton!\n"
#print(message)

passlen = int(input(message+"você quer participar,"+nome.title()+"?\n"))
if passlen == 1:
    print("bem vindo")
elif passlen != 1:
    print("q pena")
