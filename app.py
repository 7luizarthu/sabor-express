import os

restaurantes = [{'nome': 'Bar do Paulo', 'categoria': 'Bar', 'ativo': False}, {'nome': 'Restaurante da Maria', 'categoria': 'Restaurante', 'ativo': True}, {'nome': 'Lanchonete do João', 'categoria': 'Lanchonete', 'ativo': True}]


def exibir_nome_do_programa():
    '''Logotipo do App'''
    print("""
    𝑆𝑎𝑏𝑜𝑟 𝐸𝑥𝑝𝑟𝑒𝑠𝑠
    """)

def exibir_menu():
    '''Função responsável por criar o menu de lista do restaurante'''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    '''Função para encerrae encerrar o programa, quando necessário'''
    exibir_submenu('Finalizando o programa...')

def voltar_menu():
    '''Função criada com intuito de facilitar a volta ao menu principal pelo usuario'''
    input('\nPressione ENTER para voltar ao menu principal...')
    main()

def opcao_invalida():
    '''Função para informar uma opção inválida ao usuario'''
    print('Opção inválida. Tente novamente.')
    voltar_menu()
def exibir_submenu(texto):
    '''Função para exibir novamente o menu'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    Inputs: 
    - Nome do Restaurante;
    - Categoria.
    Output:
    - Adiciona um novo restaurante  a lista de restaurante.
    '''
    exibir_submenu('Cadastro de restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante "{nome_restaurante}": ')
    dados_restaurantes = ({'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False})
    restaurantes.append(dados_restaurantes)
    print(f'\nRestaurante "{nome_restaurante}" cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    '''Função para realizar a listagem de todos os restaurantes cadastrados'''
    exibir_submenu('Lista de restaurantes')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = "Ativado" if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    voltar_menu()

def alternar_status_restaurante():
    '''Função criada para o usuario alterar o estado daquele restaurante no app'''
    exibir_submenu('Ativando/Desativando restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            status = f'O restaurante "{nome_restaurante}" foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante "{nome_restaurante}" foi desativado com sucesso!'

            if not restaurante_encontrado:
                print(f'O restaurante "{nome_restaurante}" não foi encontrado.')

        voltar_menu()

def escolher_opcao():
    '''Função para validar a opção escolhida pelo usuario, e direcionar para o submenu correto'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    '''Define a ordem das etapas que aparece ao usuario'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    '''Defini a main como arquivo principal'''
    main()