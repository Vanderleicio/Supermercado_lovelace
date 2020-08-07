#Menu de cadastro do cliente
def cadastro():
    cliente = {}
    #Organiza os dados informados pelo cliente em um dicionário
    nomeCliente = input(f"Nome Completo: ")
    cliente[f"Nome"] = nomeCliente

    emailCliente = input(f"Email: ")
    emailCompare = emailCliente.count('@')
    if emailCompare != 0:
        cliente[f"Email"] = emailCliente
    else:
        print(f"Email com formato inválido. Tente novamente.")
        return


    print(f"A senha deve ser composta de uma letra maiuscúla e um número.")
    senhaCliente = input(f"Digite uma senha: ")
    senhaMinuscula = senhaCliente.islower()
    print(senhaMinuscula)

    if len(senhaCliente) > 6:
            if senhaMinuscula == True:
                print(f"A senha deve ter pelo menos uma letra maiuscúla.")
                return

            else:
                cliente[f"Senha"] = senhaCliente
    else:
        print(f"A senha deve ter no mínimo 6 caractéres.")
        return

    telefoneCliente = input(f"Telefone: ")
    cliente[f"Telefone"] = telefoneCliente

    cpfCliente = input(f"CPF (Somente números): ")
    cliente[f"CPF"] = cpfCliente

    arqCadastro = open('clienteDados.txt', 'a')

    #Salva o dicionário com os dados informados pelos clientes em um arquivo .txt
    arqCadastro.writelines(str(cliente))
    arqCadastro.write('\n')
    arqCadastro.close()


