print("Bem-vindo ao quiz sobre comunismo!")

playing = input("Você gostaria de jogar? ")

if playing.lower() != "sim":
    quit()

print("Ok! Vamos jogar :)")
score = 0

# primeira pergunta
print("Como o comunismo resolve o problema da desigualdade?")
print("a) Fazendo todos igualmente ricos em promessas")
print("b) Distribuindo igualmente a escassez, exceto para os líderes")
print("c) Criando uma nova classe alta: a burocracia do partido")

resposta = input("alternbativa correta")

if resposta != "":
    print("acertou!")
    score += 1
else:
    print("errou!")

# segunda pergunta
print("Qual é o prêmio para o empreendedor do ano em uma economia comunista?")
print("a) Uma viagem de negócios patrocinada pelo estado para aprender sobre a economia de mercado... através de documentários censurados.")
print("b) Um aperto de mão virtual do líder supremo, preservando a igualdade por não dar nada de valor.")
print("c) Uma bela placa comemorativa que diz: 'Parabéns, você quase violou a política do estado!'")
print("d) Um novo título de trabalho: 'Assistente sênior na redistribuição de suas próprias inovações.'")

resposta = input("alternbativa correta?")

if resposta != "":
    print("acertou!")
    score += 1
else:
    print("errou!")


# terceira pergunta
print("Como os países comunistas modernos lidam com a crise climática?")
print("a) O que você não pode produzir, você não pode poluir.")
print("b) Redistribuindo o smog igualmente entre a população.")
print("c) Alegando que a mudança climática é uma invenção capitalista, enquanto secretamente investe em energias renováveis")

resposta = input("alternbativa correta?")

if resposta != "":
    print("acertou!")
    score += 1
else:
    print("errou!")

if score == 3:
    print("Parabéns você já está pronto para viver em um regime comunista!")
else:
    print("Você vai ter que estudar mais para poder viver nesse mundo perfeito!")



