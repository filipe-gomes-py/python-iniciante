def menu(opcoes):
    texto = input(opcoes)
    return texto
    
def calculo(mensagem):
    opcao = float(input(mensagem))
    return opcao
    
def somar(a, b):
    return a + b
    
def subtrair(a, b):
    return a - b
    
def multiplicar(a, b):
    return a * b
    
def dividir(a, b):
    return a / b
    
def escolher_calculo(menu, a, b):
    if menu == "+":
        return somar(a, b)
    elif menu == "-":
        return subtrair(a, b)
    elif menu == "*":
        return multiplicar(a, b)
    elif menu == "/":
        return dividir(a, b)
    else:
        return None
        
def main():
    while True:
        menu = input(" Escolha a operacao que deseja fazer: (+, -, *, /) ou digite 'sair': ")
        if menu == "sair":
            break
            
        a = calculo("Digite o primeiro numero: ")
        b = calculo("Digite o segundo numero: ")
        
        resultado = escolher_calculo(menu, a, b)
        
        if resultado is None:
            print("Operacao invalida")
        else:
            print("Resultado: ", resultado)
            
main()
