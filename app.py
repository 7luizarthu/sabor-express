import os

restaurantes = [{'nome': 'Bar do Paulo', 'categoria': 'Bar', 'ativo': False}, {'nome': 'Restaurante da Maria', 'categoria': 'Restaurante', 'ativo': True}, {'nome': 'Lanchonete do João', 'categoria': 'Lanchonete', 'ativo': True}]


def exibir_nome_do_programa():
    print("""
    𝑆𝑎𝑏𝑜𝑟 𝐸𝑥𝑝𝑟𝑒𝑠𝑠
    """)

def exibir_menu():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_submenu('Finalizando o programa...')

def voltar_menu():
    input('\nPressione ENTER para voltar ao menu principal...')
    main()

def opcao_invalida():
    print('Opção inválida. Tente novamente.')
    voltar_menu()
def exibir_submenu(texto):
    os.system('cls')
    print(texto)

def cadastrar_restaurante():
    exibir_submenu('Cadastro de restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante "{nome_restaurante}": ')
    dados_restaurantes = ({'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False})
    restaurantes.append(dados_restaurantes)
    print(f'\nRestaurante "{nome_restaurante}" cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    exibir_submenu('Lista de restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria_restaurante} | {ativo_restaurante} - {ativo_restaurante}')
    voltar_menu()

def alternar_status_restaurante():
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
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()