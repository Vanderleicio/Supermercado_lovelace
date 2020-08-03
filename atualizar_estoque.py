with open('produtosAda.txt', 'r+') as arquivo:
    lista = []
    for linha in arquivo:
        linhas = linha.rstrip().split(';')
        lista.append(linhas)
    print(lista)

def alterar_estoque(n):
    while n:
        if n == 1:
            lista[int(input('Digite o código do produto que deseja alterar, sem zeros: '))][3] = int(input('Digite a quantidade de produtos atualizada: '))
            print(lista)
            n = int(input('[1] Atualizar Estoque \n[2] Sair: '))

        if n == 2:
            print('Alterações Salvas.')
            break

        if n != 1 and n != 2:
            print('Escolha uma opção válida')
            n = int(input('[1] Atualizar Estoque \n[2] Sair: '))

n = int(input('[1] Atualizar Estoque \n[2] Sair: '))
alterar_estoque(n)

novo_arquivo = open('produtosAdaNEW.txt', 'w')
novo_arquivo.write(str(lista))
novo_arquivo.close()
