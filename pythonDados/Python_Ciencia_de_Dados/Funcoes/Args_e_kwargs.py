#Quando passarmos (**) dois asteristicos kwargs estamos dizendo que é um dicionario 
#Quando passarmos (*) um asteristico args é uma tupla ou lista

def exibir_poema(data_extenso,*args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

    exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor = "Tim Peters", ano = 1999)