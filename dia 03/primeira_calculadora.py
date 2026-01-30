print("Calculadora")

def ler_numero(mensagem) :
    texto = float(input(mensagem))
    return texto
    
def somar(n1, n2):
    return n1 + n2
    
def subtrair(n1, n2):
    return n1 - n2
    
def multiplicar(n1, n2):
    return n1 * n2
    
def dividir(n1, n2):
    return n1 / n2
    
def escolher_operacao(op, n1, n2):
    if op == "+":
        return somar(n1, n2)
    elif op == "-":
        return subtrair(n1, n2)
    elif op == "*":
        return multiplicar(n1, n2)
    elif op == "/":
        return dividir(n1, n2)
    else:
        return None
        
def main():
    op = input("Escolha a operaçao (+, -, *, /): ")
    n1 = ler_numero("Digite o primeiro numero: ")
    n2 = ler_numero("Digite o segundo numero: ")
    resultado = escolher_operacao(op, n1, n2)
    if resultado is None:
        print("Operaçao invalida. ")
    else:
        print("Resultado: ", resultado )
        
main()
