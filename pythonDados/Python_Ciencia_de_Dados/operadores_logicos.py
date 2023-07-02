print(True and True)
print(True and False)
print(True or True)
print(True or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

#forma errada de fazer dificil leitura
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)


#boa pratica
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)


