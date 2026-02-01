def seu_login(login):
    texto = input(login)
    return texto
    
def sua_senha(senha):
    resposta = input(senha)
    return resposta
    
def main_login():
    login = input("Crie seu login: ")
    while True:
        login_correto = input("Digite seu login: ")
        if login_correto != login:
            print("Login invalido, tente novamente! ")
        else:
            break
def main_senha():            
    senha = input("Crie sua senha: ")
    while True:
        if len(senha) < 8:
            print("Senha invalida. Minimo de 8 caracteres.")
        elif len(senha) >= 8:
            senha_correta = input("Digite sua senha: ")
            if senha_correta != senha:
                print("Senha invalida. ")
            else:
                print("Senha e Login validados! ")
                break
    
main_login()
main_senha()
