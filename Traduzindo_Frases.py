textSpeakDictionary = {
    "rs"    : "risos" ,
    "tmb"   : "também" 
}

#obtém a frase para tradução
sentence = input("Insira uma frase para traduzir: ").lower()

#divide a frase em uma lista de palavras
wordsToTranslate = sentence.split()

translatedSentence = ""

#passa por cada palavra da lista
for word in wordsToTranslate:

    #adiciona a palavra traduzida caso ela exista no dicionário
    if word in textSpeakDictionary:

        translatedSentence += textSpeakDictionary[word] + " "
    
    #mantém a palavra original caso não exista tradução
    else:

        translatedSentence += word + " "

#imprime a frase traduzida
print("==>")
print(translatedSentence)