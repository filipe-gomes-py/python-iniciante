lista = []

while True:
    item = input("Adicione um item a sua lista! (ou 'sair' para terminar): ")
    item_limpo = item.strip().lower()
    
    if item_limpo == "sair":
        break
        
    lista.append(item.strip())
        
print("Lista de mercado")
for coisa in lista:
        print("-", coisa)
