conta_normal = True
conta_universitaria = True

cheque_especial = 450
saldo = 2000
saque = 2500

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel o saque")
elif conta_universitaria: 
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente!")