def adicionar():  # Menu para adicionar itens ao carrinho.
    print('Aqui você pode adicionar um novo produto ao seu carrinho\n'
          'Para isso digite o código dele com base na lista abaixo: ')
    print('\n\n')
    mostrar_produtos_disponiveis(produtos, 60)  # Mostra a lista de produtos.
    separar()
    while True:
        codigo = input('Digite o código do produto: ')
        while not checar_codigo(codigo):  # Verifica se o código digitado é valido.
            codigo = input('Código não encontrado. Por favor, tente novamente: ')
        produto_escolhido = selecionar_produto(codigo)
        if produto_escolhido:  # Verifica se a lista com o produto escolhido tem algum item nela.
            quantidade = int(input('Digite a quantidade desejada: '))
            while quantidade <= 0 or quantidade > produto_escolhido['estoque']:  # Verificar se a quantidade é válida.
                quantidade = int(input('Quantidade não disponível.Por favor, tente novamente: '))
            produto_escolhido['quantidade'] = quantidade  # Coloca a quantos ítens serão comprados.
            carrinho.append(produto_escolhido)  # Adiciona o produto ao carrinho
            print('Produto adicionado com sucesso!')
        if nao_deseja_continuar('Deseja adicionar mais um produto? (Sim/Não)', 'Opção inválida. Digite sim ou não: '):
            break
    separar()
    menu()


def alterar():  # Altera a quantidade de um produto.
    while True:
        print('Esses são os produtos no seu carrinho até o momento:')
        mostrar_produtos_disponiveis(carrinho)
        posicao = int(input(f'Digite a posição do produto que você deseja '
                            f'alterar a quantidade. (De 1 até {len(carrinho)}): '))
        while not 1 <= posicao <= len(carrinho):
            posicao = int(input(f'Posição inválida. Digite uma posição entre 1 e {len(carrinho)}'))
        nova_quantidade = int(input('Digite a nova quantidade: '))
        while nova_quantidade <= 0 \
                or nova_quantidade > carrinho[posicao - 1]['estoque']:  # Verifica a validade da quantidade escolhida.
            nova_quantidade = int(input('Quantidade não disponível.Por favor, tente novamente: '))
        carrinho[posicao - 1]['quantidade'] = nova_quantidade
        if nao_deseja_continuar('Deseja alterar a quantidade de outro produto? (Sim/Não) ',
                                'Opção inválida. Digite sim ou não: '):
            break
    separar()
    menu()


def atualizar_estoque():  # Atualiza o arquivo com o estoque novo.
    with open('produtosAda.txt', 'w', encoding='UTF-8') as arquivo:
        colunas = ['código', 'produto', 'preço', 'estoque']
        for chave in colunas:
            arquivo.write(chave)
            if chave != 'estoque':
                arquivo.write(';')
            else:
                arquivo.write('\n')
        for produto in produtos:
            for chave in colunas:
                if chave == 'preço':
                    arquivo.write('{0:.2f}'.format(produto[chave]))
                else:
                    arquivo.write(str(produto[chave]))
                if chave != 'estoque':
                    arquivo.write(';')
                else:
                    arquivo.write('\n')


def checar_codigo(codigo):  # Retorna True se o código é válido e False se não for.
    for produto in produtos:
        if produto['código'] == codigo:
            return True
    else:
        return False


def emitir_nota_fiscal():  # Emite a nota fiscal de cada cliente.
    with open('nota_fiscal.txt', 'w', encoding='UTF-8') as arq:
        total = 0
        arq.write('Supermercado Ada Lovelace.'.center(50) + '\n')
        arq.write('-=' * 25 + '\n')
        arq.write('CPF do cliente: ' + cpf + '\n')
        arq.write('-=' * 25 + '\n')
        arq.write('Quantidade'.ljust(18) + 'Produto'.ljust(20) + 'Preço total' + '\n')
        arq.write('-=' * 25 + '\n')
        for j in range(len(carrinho)):
            quantidade = carrinho[j]['quantidade']
            preco = round(quantidade * carrinho[j]['preço'], 2)
            total += preco
            arq.write(carrinho[j]['produto'].ljust(20) + str(quantidade).ljust(18) +
                      ('R$ ' + '{0:.2f}'.format(preco)).ljust(18) + '\n')
        arq.write('-=' * 25 + '\n')
        arq.write(f'TOTAL DA CONTA: R${total:.2f}' + '\n')
    print('O ARQUIVO DA NOTA FISCAL JÁ FOI GERADO')


def filtro():  # Ativa ou desativa o filtro por preço.
    global filtrar, produtos
    if filtrar:
        print('A partir de agora os produtos NÃO serão mais exibidos por ordem de preço!')
        filtrar = False
        produtos = transformar_produtos_em_lista()
    else:
        print('A partir de agora os produtos SERÃO exibidos por ordem de preço!')
        filtrar = True
        produtos = ordenar_produtos_por_preco()
    menu()


def finalizar():  # Finaliza as compras.
    emitir_nota_fiscal()
    retirar_do_estoque()
    atualizar_estoque()


def menu():
    print('O que você deseja fazer?\n'
          '[0] Adicionar um produto ao seu carrinho.\n'
          '[1] Remover um produto do seu carrinho.\n'
          '[2] Alterar quantidades de um produto.\n'
          '[3] Finalizar a compra.\n'
          '[4] Ligar/desligar o filtro da lista de produtos pelo preço.\n'
          '[5] Cancelar compras.')
    opcao = input('Digite a opção desejada: ')
    while opcao not in '012345':
        opcao = input('Opção inválida. Digite alguma das opções fornecidas.')
    if not carrinho and opcao in '123':
        separar()
        print('Não há nenhum produto no seu carrinho ainda.')
        separar()
        menu()
    else:
        separar()
        if opcao == '0':
            adicionar()
        elif opcao == '1':
            remover()
        elif opcao == '2':
            alterar()
        elif opcao == '3':
            finalizar()
        elif opcao == '4':
            filtro()
        else:
            print('Tchau, até mais!')
        print('Obrigado por usar nosso sistema!')
        exit()


def mostrar_produtos_disponiveis(lista_produtos, tamanho_dos_atributos=80):  # Exibe a lista de produtos.
    print('-' * tamanho_dos_atributos)
    for chave in lista_produtos[0]:
        if chave != 'estoque':
            print(chave.ljust(25), end='')
    print()
    print('-' * tamanho_dos_atributos)
    for i in range(len(lista_produtos)):
        for elementos in lista_produtos[i]:
            if elementos != 'estoque':
                if elementos == 'preço':
                    print('R$ {0:.2f}'.format(lista_produtos[i][elementos]).ljust(25), end='')
                else:
                    print(str(lista_produtos[i][elementos]).ljust(25), end='')
        print()


def nao_deseja_continuar(mensagem1, mensagem2):
    continuar = input(mensagem1).strip().upper()[0]
    while continuar not in 'SN':
        continuar = input(mensagem2).strip().upper()[0]
    if continuar == 'N':
        return True


def ordenar_produtos_por_preco():  # Ordena os produtos do menor para o maior preço e retorna uma lista ordenada deles.
    lista_ordenada = []
    numero_de_produtos = len(produtos)
    for i in range(numero_de_produtos):  # Variável para a leitura dos produtos na lista desordenada.
        if i == 0:
            lista_ordenada.append(produtos[0])
        else:
            for j in range(len(lista_ordenada)):  # Variável para leitura dos produtos na lista ordenada.
                if produtos[i]['preço'] < lista_ordenada[j]['preço']:
                    lista_ordenada.insert(j, produtos[i])  # Coloca o produto com menor preço na frente.
                    break
            else:
                lista_ordenada.append(produtos[i])
    return lista_ordenada


def remover():  # Remove produtos do carrinho.
    while True:
        if not carrinho:  # Verifica se ainda tem itens para remover.
            print('Você não tem mais produtos para remover!')
            break
        else:
            print('Esses são os produtos que estão no seu carrinho até o momento:')
            mostrar_produtos_disponiveis(carrinho)
            posicao = int(input(f'Digite a posição do produto'
                                f' que você deseja remover. (De 1 até {len(carrinho)}): '))
            while not 1 <= posicao <= len(carrinho):  # Verifica se a posição é válida
                posicao = int(input(f'Posição inválida. Digite uma posição entre 1 e {len(carrinho)}'))
            carrinho.pop(posicao - 1)  # Retira o produto do carrinho.
            print('Remoção executada com sucesso.')
            if carrinho:  # Verifica se o carrinho está vazio, para poder exibir a lista dos itens restantes.
                print('Esses são os seus produtos agora:')
                mostrar_produtos_disponiveis(carrinho)
            if nao_deseja_continuar('Deseja remover mais um produto(Sim/Não)? ', 'Opção inválida. Digite sim ou não: '):
                break
    separar()
    menu()


def retirar_do_estoque():  # Retira o número de ítens comprados da lista de produtos.
    for i in range(len(carrinho)):
        for produto in produtos:
            if carrinho[i]['código'] == produto['código']:
                produto['estoque'] -= carrinho[i]['quantidade']


def selecionar_produto(codigo):  # Seleciona o produto escolhido depois de ter o seu código checado.
    for i in range(len(produtos)):
        if produtos[i]['código'] == codigo:
            if produtos[i]['estoque'] == 0:  # Verifica a disponibilidade do produto.
                print('Desculpe! Estamos sem esse produto no momento!')
                return False
            else:
                produto_escolhido = produtos[i]
                return produto_escolhido


def separar():  # Separador visual.
    print()
    print('-=' * 30)
    print()


def transformar_produtos_em_lista():  # Converte o arquivo em uma lista de listas.
    estoque = []
    with open('produtosAda.txt', 'r', encoding='UTF-8') as arquivo:
        arquivo.readline()
        colunas = ['código', 'produto', 'preço', 'estoque']
        for linha in arquivo:
            produto = {}
            ponto_de_partida = 0  # Ponto que inicia a leitura para separar as características do produto.
            contador_separador = 0  # Conta os separadores na linha, para definir os nomes das chaves.
            for i in range(len(linha)):
                if linha[i] == ';' or linha[i] == '\n':  # Identifica o separador usado no arquivo ou o fim da linha.
                    caracteristica = linha[ponto_de_partida:i]  # Separa uma única característica do produto.
                    if colunas[contador_separador] == 'preço':
                        caracteristica = round(float(caracteristica), 2)
                    elif colunas[contador_separador] == 'estoque':
                        caracteristica = int(caracteristica)
                    produto[colunas[contador_separador]] = caracteristica
                    contador_separador += 1
                    ponto_de_partida = i + 1  # Atualiza o ponto de partida para o início da próxima característica.
            if contador_separador != 4:
                produto['estoque'] = 0
            estoque.append(produto)
    return estoque


cpf = '123456789'
filtrar = False
carrinho = []
produtos = transformar_produtos_em_lista()
menu()
