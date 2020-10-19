tabela20CORITIBA20Dictionary = {
    "INTERNACIONAL"    : "34",
    "FLAMENGO"         : "34",
    "ATLÉTICO-MG"      : "31",
    "SÃO PAULO"        : "27",
    "SANTOS"           : "27",
    "FLUMINENSE"       : "26",
    "FORTALEZA"        : "24",
    "PALMEIRAS"        : "22",
    "ATLÉTICO-GO"      : "22",
    "GRÊMIO"           : "21",
    "SPORT RECIFE"     : "20",
    "CEARÁ SC"         : "19",
    "VASCO DA GAMA"    : "18",
    "CORINTHIANS"      : "18",
    "BOTAFOGO"         : "18",
    "BAHIA"            : "16",
    "ATHETICO-PR"      : "16",
    "CORITIBA"         : "16",
    "BRAGANTINO-SP"    : "16",
    "GOIÁS"            : "10"
}
print(f'{"Tabela Brasileião 2020":^30}')
print('='*40)

sentence = input("Digite o nome de um time ou T para ver a tabela completa: ").upper()

if sentence == 'INTERNACIONAL':
    p = 1
elif sentence == 'FLAMENGO':
    p = 2
elif sentence == 'ATLÉTICO-MG':
    p = 3
elif sentence == 'SÃO PAULO':
    p = 4
elif sentence == 'SANTOS':
    p = 5
elif sentence == 'FLUMINENSE':
    p = 6
elif sentence == 'FORTALEZA':
    p = 7
elif sentence == 'PALMEIRAS':
    p = 8
elif sentence == 'ATLÉTICO-GO':
    p = 9
elif sentence == 'GRÊMIO':
    p = 10
elif sentence == 'SPORT RECIFE':
    p = 11
elif sentence == 'CEARÁ SC':
    p = 12
elif sentence == 'VASCO DA GAMA':
    p = 13
elif sentence == 'CORINTHIANS':
    p = 14
elif sentence == 'BOTAFOGO':
    p = 15
elif sentence == 'BAHIA':
    p = 16
elif sentence == 'ATHLETICO-PR':
    p = 17
elif sentence == 'CORITIBA':
    p = 18
elif sentence == 'BRAGANTINO-SP':
    p = 19
elif sentence == 'GOIÁS':
    p = 20

elif sentence == 'T':
    print('='*40)
    for tabela in tabela20CORITIBA20Dictionary:
        print(f'{tabela:.<30} ', end='')
        print(f'{tabela20CORITIBA20Dictionary[tabela]} Pontos')
    print('='*40)
else:
    print('Opção invalida')

#divide a frase em uma lista de palavras
wordsToTranslate = sentence.split()

translatedSentence = ""

#passa por cada palavra da lista
for word in wordsToTranslate:

    #adiciona a palavra traduzida caso ela exista no dicionário
    if word in tabela20CORITIBA20Dictionary:

        translatedSentence += tabela20CORITIBA20Dictionary[word] + ""
    
    #mantém a palavra original caso não exista tradução
    else:

        translatedSentence += word + " "


print(f'{sentence} está na {p}ª posição com {translatedSentence} pontos')