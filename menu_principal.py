from time import sleep
from cadastro_do_usuario import cadastro
from menu_compras import menu_login
from atualizar_estoque import menu_login_funcionario


def linha(titulos):
    print('-=' * 25)
    print(titulos)
    print('-=' * 25)


# comando principal


def menu(opc_usuario='0'):
    while opc_usuario != '4':
        print(f'{"SUPERMERCADO LOVELACE":^50}')
        linha(f'\n{"Seja bem-vindo! Escolha a sua opção:":^50}\n\n'
              '[1] Fazer cadastro de cliente.\n'
              '[2] Fazer login para cliente.\n'
              '[3] Fazer login para funcionário.\n'
              '[4] Finalizar programa.\n')
        sleep(1)
        opc_usuario = input('Digite sua opção: ')
        while opc_usuario not in '1234':
            opc_usuario = input('Opção incorreta, digite novamente: ')
        if opc_usuario == '1':
            cadastro()
        elif opc_usuario == '2':
            menu_login()
        elif opc_usuario == '3':
            menu_login_funcionario()
        else:
            print('Saindo do programa...')
            sleep(1)
    print('Obrigado pela visita, volte sempre!')


menu()
