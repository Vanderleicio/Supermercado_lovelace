# Menu de cadastro do cliente


def cadastro():
    cliente = {}
    # Organiza os dados informados pelo cliente em um dicionário
    nome_cliente = input(f"Nome Completo: ")
    cliente[f"Nome"] = nome_cliente

    email_cliente = input(f"Email: ")
    email_compare = email_cliente.count('@')
    if email_compare != 0:
        cliente[f"Email"] = email_cliente
    else:
        print(f"Email com formato inválido. Tente novamente.")
        return

    print(f"A senha deve ser composta de pelo menos uma letra maiuscúla e um número.")
    senha_cliente = input(f"Digite uma senha: ")
    senha_minuscula = senha_cliente.islower()
    if len(senha_cliente) > 6:
        if senha_minuscula:
            print(f"A senha deve ter pelo menos uma letra maiuscúla.")
            return

        else:
            cliente[f"Senha"] = senha_cliente
    else:
        print(f"A senha deve ter no mínimo 6 caractéres.")
        return

    telefone_cliente = input(f"Telefone: ")
    cliente[f"Telefone"] = telefone_cliente

    cpf_cliente = input(f"CPF (Somente números): ")
    cliente[f"CPF"] = cpf_cliente

    arq_cadastro = open('clienteDados.txt', 'a')

    # Salva o dicionário com os dados informados pelos clientes em um arquivo .txt
    arq_cadastro.writelines(str(cliente))
    arq_cadastro.write('\n')
    arq_cadastro.close()
