# Abre o arquivo .txt com os produtos em estoque e salva em uma lista
with open('produtosAda.txt', 'r+', encoding='UTF-8') as arquivo:
    lista = []
    for linha in arquivo:
        linhas = linha.rstrip().split(';')
        lista.append(linhas)

# Altera a quantidade dos produtos em estoque.
# Se o código do produto for igual ao código digitado é possível alterar a quantidade em estoque.


def alterar_estoque():
    n = int(input('[1] Atualizar Estoque \n[2] Sair\n--> '))
    while n:
        codigo = input('Digite o código do produto que deseja alterar: ')
        for produto in lista:
            if produto[0] == codigo:
                produto[3] = input('Digite a quantidade de produtos atualizada: ')
                break
        else:
            print('Código inválido. Tente novamente.')
        print()
        n = int(input('[1] Atualizar Estoque \n[2] Sair\n--> '))

        if n == 2:
            print('Alterações Salvas.')
            atualizar_estoque()
            break

        if n != 1 and n != 2:
            print('Escolha uma opção válida')
            n = int(input('[1] Atualizar Estoque \n[2] Sair\n--> '))

# Menu de login para funcionários através do Código de Funcionário e Senha.


def menu_login_funcionario():
    print('Para fazer login, por favor, digite as suas informações abaixo:')
    while True:
        print('Código de funcionário:')
        print('--> ', end='')
        login = input('')
        print('Senha (cuidado com as letras maiúsculas/minúsculas):')
        print('--> ', end='')
        senha = input('')
        if valida_informacoes(login, senha):  # Valida o login e libera acesso à função de alterar estoque.
            alterar_estoque()
            break
        print()
        print('Login e/ou senha incorretos.\n'
              'Cheque suas informações e tente novamente:')

# Verifica se as informações de Código de Funcionário e Senha estão no cadastro de funcionários.
# Retorna "True" ou "False" para funcionários cadastrados ou não cadastrados.


def valida_informacoes(login, senha):
    for funcionario in funcionarios:
        if login == funcionario['codigoFuncionario']:
            if senha == funcionario['senha']:
                return True
            else:
                return False
    return False

# Lê os dados de cadastro de funcionários.
# Armazena os dados de maneira ordenada em uma lista.


def arquivo_para_lista():
    lista_funcionario = []
    with open('funcionariosAda.txt', 'r', encoding='UTF-8') as arq:
        arq.readline()
        colunas = ['codigoFuncionario', 'nome', 'senha']
        for linhas_arq in arq:
            funcionario = {}
            ponto_de_partida = 0
            contador_separador = 0
            for i in range(len(linhas_arq)):
                if linhas_arq[i] == ';' or linhas_arq[i] == '\n' or linhas_arq[i] == ':':
                    caracteristica = linhas_arq[ponto_de_partida:i]
                    funcionario[colunas[contador_separador]] = caracteristica
                    contador_separador += 1
                    ponto_de_partida = i + 1
            lista_funcionario.append(funcionario)
    return lista_funcionario

# Atualiza ("salva") o arquivo com as modificações no estoque.


def atualizar_estoque():
    with open('produtosAda.txt', 'w', encoding='UTF-8') as arquivo2:
        for produto in lista:
            for i in range(len(produto)):
                arquivo2.write(produto[i])
                if i != 3:
                    arquivo2.write(';')
                else:
                    arquivo2.write('\n')


funcionarios = arquivo_para_lista()
