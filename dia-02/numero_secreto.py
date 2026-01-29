numero_secreto = 7

while True:
    pergunta = int(input("Adivinha o numero secreto de 1 a 10 "))
 
    if pergunta == numero_secreto:
        print("Parabens! Voce acertou.")
        break
    else:
        print("Voce errou, tente novamente!")
