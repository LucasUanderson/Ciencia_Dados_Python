MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar a CNH,..")
else:
    print("Ainda não pode tirar a CNH. ")


    
if idade >= 18:
    print("Maior de idade, pode tirar a CNH,..")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulass práticas.")
else:
    print("Ainda não pode tirar a CNH. ")