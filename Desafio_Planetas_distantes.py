textSpeakDictionary = {
    "mercúrio"    : "77.3 Milhões" ,
    "vênus"   : "41 Milhões" ,
    "marte"    : "62.07 Milhões" ,
    "júpiter"    : "778 Milhões",
    "saturno"    : "1.4 Bilhões",
    "urano"   : "2.720.400.000",
    "neturno"   : "4 Bilhões"
    
}

#obtém a frase para tradução
sentence = input("Digite um planeta: ").lower()

#divide a frase em uma lista de palavras
wordsToTranslate = sentence.split()

translatedSentence = ""

#passa por cada palavra da lista
for word in wordsToTranslate:

    #adiciona a palavra traduzida caso ela exista no dicionário
    if word in textSpeakDictionary:

        translatedSentence += textSpeakDictionary[word] + ""
    
    #mantém a palavra original caso não exista tradução
    else:

        translatedSentence += word + " "

#imprime a frase traduzida
print(f'{sentence} está a {translatedSentence} km da Terra')