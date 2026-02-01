def main():
    while True:
        senha = input("Crie uma senha: ")
        if len(senha) < 8:
            print("Senha invalida *Deve conter no minimo 8 caracteres* ")
        elif len(senha) == 0:
            print("Senha invalida *Deve conter no minimo 8 caracteres* ")
        else:
            print("Senha criada com sucesso! ")
            return senha
            break
main()
