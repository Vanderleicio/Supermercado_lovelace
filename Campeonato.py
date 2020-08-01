from time import sleep
def linha(titulos):
    print('-'*40)
    print(titulos)
    print('-'*40)
#comando principal
def menu(opc_usuario=0):
    while (opc_usuario != 4):
        print(f'{"SUPERMERCADO ADA LOVELACE":^45}')
        linha('[1] Fazer o cadastro de clientes\n[2] Fazer login de clientes\n[3] Fazer login de funcionário\n[4] Sair')
        while True:
            opc_usuario = int(input(('Digite sua opção: ')))
            while opc_usuario not in (1,2,3,4):
                print('Opção incorreta, digite novamente.')
                opc_usuario = int(input(('Digite sua opção: ')))
            if opc_usuario == 1:
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
            elif opc_usuario == 2:
                break
            elif opc_usuario == 3:
                break
            else:
                print('Saindo...')
                sleep(1)
                break
    print('Obrigado pela visita, volte sempre!')
menu()


              
