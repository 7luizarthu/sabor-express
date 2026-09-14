import os

restaurantes = ['Pizza', 'Hamburguer', 'Churrasco', 'Sushi']

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
    print('Encerrando o programa...')
    os.system('cls')

def opcao_invalida():
    print('Opção inválida. Tente novamente.')
    input('Pressione ENTER para voltar ao menu principal...')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante "{nome_restaurante}" foi cadastrado com sucesso!')
    input('\nPressione ENTER para voltar ao menu principal...')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Lista de restaurantes cadastrados:')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    input('\nPressione ENTER para voltar ao menu principal...')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
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