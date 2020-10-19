passwordDictionary = {
    "programador"   : "acesso" ,
    "felipe"        : "felipe123" ,
    "daiana"        : "sousa19",
    "sousadaiana"   : "sousa040896"
}

print("Programa super secreto")
print("="*15)

loginAttempts = 0
cont = 3
while loginAttempts < 3:
    nome = input("Nome : ")
    senha = input("senha : ")
    if nome in passwordDictionary and senha == passwordDictionary[nome]:
        print(f'BEM-VINDO {nome.upper()}')
        loginAttempts = 3
    else:
        loginAttempts += 1
        cont -= 1
        if loginAttempts <= 2:
            print(f'Usuario ou Senha Invalida, Tentativas restantes {cont}')
        elif loginAttempts == 3:
            print('Usuario não encontrado')
