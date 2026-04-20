usuarios = {"admin": "s89898"}
contador = 3

while True:
    print("\n" + "-"*26)
    print("      PAINEL DE LOGIN")
    print("-"*26)
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Sair")
    
    escolha = input("\nEscolha uma das opções: ").strip()
    print("-"*26)

    if escolha == "1":
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario in usuarios and usuarios[usuario] == senha:
    
            print(f"✅ Login {usuario}, bem-sucedido!")
            contador = 3
        else:
            contador = contador - 1
            if contador > 0:
                print("❌ Usuário ou senha incorretos.")
                print(f"Voce tem mais {contador} de 3")
            else:
                print("Seu acesso foi bloqueado 🚫")
                break

    elif escolha == "2":
        print("PReencha as informações de CADASTRO:")
        novo_usuario = input("Nome de usuário desejado: ")
        
        if novo_usuario in usuarios:
            print("⚠️ Este usuário já existe!")
        else:
            nova_senha = input("Senha desejada: ")
            print(f"\nConfirme: Usuário [{novo_usuario}]")
            
            confirmacao = input("Confirmar cadastro? (SIM/NAO): ").lower().strip()

            if confirmacao == "sim":
                usuarios[novo_usuario] = nova_senha
                print("✅ Cadastro realizado com sucesso!")
            else:
                print("⚠️ Cadastro cancelado.")

    elif escolha == "3":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")
