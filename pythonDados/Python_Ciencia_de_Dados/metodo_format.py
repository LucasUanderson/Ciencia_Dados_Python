nome = "Lucas"
idade = 26
profissao = "Programador"
linguagem = "Python"


# melhor forma de formatar strings
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Outra forma de formato indicando posição
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format (nome, idade,profissao,linguagem))

# Outra forma de formato indicando posição
print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format (nome, idade,profissao,linguagem))


# Outra forma de formato indicando posição
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format (nome = nome, idade = idade ,profissao = profissao,linguagem = linguagem))



# Outra forma de formato indicando posição
print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format (nome, idade,profissao,linguagem))







