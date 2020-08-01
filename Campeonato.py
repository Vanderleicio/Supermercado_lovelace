
def cadastro():
    cliente = {}

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
    arqCadastro.writelines(str(cliente))
    arqCadastro.write('\n')
    arqCadastro.close()


