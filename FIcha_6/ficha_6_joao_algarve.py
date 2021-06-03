"""
Trabalho realizado por:
        João Algarve
        PDM-B
        1º ano
        nº 45304
"""
#--------------------------------1--------------------------------
var = input("Escreva algo: ")

vogais_count = {}

for vogais in "aeiou":
    count = var.count(vogais)
    vogais_count[vogais] = count

print("Ocorrência da Vogal a: {0}\n"
      "Ocorrência da Vogal e: {1}\n"
      "Ocorrência da Vogal i: {2}\n"
      "Ocorrência da Vogal o: {3}\n"
      "Ocorrência da Vogal u: {4}\n".format(vogais_count["a"],
                                            vogais_count["e"],
                                            vogais_count["i"],
                                            vogais_count["o"],
                                            vogais_count["u"]))
#--------------------------------1--------------------------------


#--------------------------------2--------------------------------

var_ex2 = 'a ana e o aniceto foram ao cinema anadia'

print(var_ex2.replace("ana", ""))

#--------------------------------2--------------------------------


#--------------------------------3--------------------------------

var_ex3 = input('\nEscreva uma frase: ')

print(var_ex3)

print(var_ex3.replace(" ", ""))

#--------------------------------3--------------------------------


#--------------------------------4--------------------------------

var_ex4 = input('\nEscreva uma frase: ')

print(var_ex4)

print(var_ex4.replace(" ", "##"))

#--------------------------------4--------------------------------