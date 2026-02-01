def calculo_media(notas):
    if len(notas) == 0:
        return 0
    total = sum(notas)
    return total / len(notas)
    
    
def receber_notas():
    lista = []
    while True:
        nota = input("Adicione uma nota ou digite 'sair': ")
        if nota == "sair":
            break
        else:
            nota_float = float(nota)
            lista.append(nota_float)
    return lista

def main():
    print("Boletim!")
    notas = receber_notas()
    media = calculo_media(notas)
    print("Sua media foi:", media)
    if calculo_media(notas) >= 6:
        print("Aprovado! ")
    else:
        print("Reprovado! ")
        
main()
