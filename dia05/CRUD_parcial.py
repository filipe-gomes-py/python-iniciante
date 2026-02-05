def menu():
    print("\n=== MENU ===")
    print("1 -- Adicionar tarefa")
    print("2 -- Mostrar lista de tarefas")
    print("0 -- Sair ")
    
def mostrar(lista):
    for i in lista:
        print(i)
        
def main():
    lista = []
    while True:
        menu()
        opcao = input("Escolha uma opcao: ")
        if opcao == "0":
            break
        elif opcao == "1":
            item =input("Digite o item: ")
            lista.append(item)
        elif opcao == "2":
            mostrar(lista)
        else:
            print("Opcao invalida. Tente novamente!")
            
main()
