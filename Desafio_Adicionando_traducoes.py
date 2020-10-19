textSpeakDictionary = {
    "rs"    : "risos" ,
    "tbm"   : "também" ,
    "vc"    : "você" ,
    "pq"    : "porque",
    "mb"    : "muito bom",
    "vlw"   : "valeu",
    "fdp"   : "filho da Puta",
    "ñ"     : "não",
    "s"     : "sim",
    "pfv"   : "por favor",
    "tchl"  : "tchal",
    "bjs"   : "beijos",
    "sqñ"   : "só que não",
    "tlg"   : "ta ligado",
    "blz"   : "beleza"
    
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