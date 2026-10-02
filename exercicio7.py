senha_secreta = "python123"

while True:
    tentativa = input("Digite a senha secreta: ")
    
    if tentativa == senha_secreta:
        print("Acesso Liberado")
        break  
    else:
        print("Senha incorreta! Tente novamente.")
