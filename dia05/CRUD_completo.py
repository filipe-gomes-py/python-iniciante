def menu():
    print("\n == MENU == ")
    print("1 - Adicionar tarefa")
    print("2 - Mostrar lista")
    print("3 - Remover tarefas")
    print("0 - Sair")
    
def mostrar(lista):
    for i in lista:
        print(i)
        
def main():
    lista = []
    
    while True:
        menu()
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            coisa = input("Digite o que deseja adicionar: ")
            lista.append(coisa)
        elif opcao == "2":
            itens = mostrar(lista)
            print(itens)
        elif opcao == "3":
            print(lista)
            for i,item in enumerate(lista):
                print(i, "-", item)
            remover = int(input("Digite o que deseja remover: "))
            lista.pop(remover)
            print("Item removido: ", remover)
            print("Lista atual: ", lista)
        elif opcao == "0":
            break
        else:
            print("Opcao invalida. Tente novamente!")
            
main()
