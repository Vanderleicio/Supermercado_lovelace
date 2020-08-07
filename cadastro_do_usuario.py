#Menu de cadastro do cliente
def cadastro():
    cliente = {}

    #Organiza os dados informados pelo cliente em um dicionário
    nomeCliente = input(f"Nome Completo: ")
    cliente[f"Nome"] = nomeCliente

    emailCliente = input(f"Email: ")
    cliente[f"Email"] = emailCliente

    senhaCliente = input(f"Digite uma senha: ")
    cliente[f"Senha"] = senhaCliente


    telefoneCliente = input(f"Telefone: ")
    cliente[f"Telefone"] = telefoneCliente

    cpfCliente = input(f"CPF (Somente números): ")
    cliente[f"CPF"] = cpfCliente

    arqCadastro = open('clienteDados.txt', 'a')

    #Salva o dicionário com os dados informados pelos clientes em um arquivo .txt
    arqCadastro.writelines(str(cliente))
    arqCadastro.write('\n')
    arqCadastro.close()


