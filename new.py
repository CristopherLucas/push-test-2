import os


class Modulo():
    def finalizar_app(self):
        print('Encerrando o programa\n')

    def voltar_menu(self):
        input('\nDigite alguma tecla para voltar ao menu inicial: ')
        os.system('cls')
        App.main(self)

    def opcao_invalida(self):
        print('Você selecinou uma opção inválida.')
        Modulo.voltar_menu(self)

    def cadastrar_restaurante(self, list_):
        os.system('cls')
        nome = input('''Cadastro de Restaurantes

Insira o nome do restaurante que deseja cadastrar: ''').title()
        categoria = input('Digite a categoria do restaurente: ')
        list_.append({'nome': nome, 'categoria': categoria, 'ativo': False})
        os.system('cls')
        print(f'O restaurente {nome} foi adicionado.')
        Modulo.voltar_menu(self)
        return list_

    def listar_restaurante(self, list_):
        print('Listando restaurantes\n\n')
        print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(22)}\n')
        for restaurante in list_:
            print(
                f'- {restaurante["nome"].ljust(20)} |\
{restaurante["categoria"].ljust(20)} | ', end='')
            print(
                'O restaurante está ativo' if restaurante['ativo']
                else 'O restaurante está inativo')
        Modulo.voltar_menu(self)

    def alterar_estado(self, list_):
        restaurante_encontrado = False
        nome = input(
            'Digite o nome do restaurante que deseja ativar: ').title()
        for restaurante in list_:
            if nome == restaurante['nome']:
                restaurante_encontrado = True
                restaurante['ativo'] = not restaurante['ativo']
                os.system('cls')
                print(
                    f'O restaurante {nome} foi ativado com sucesso!' if restaurante['ativo']
                    else f'O restante {nome} foi desativado com sucesso!')
        if not restaurante_encontrado:
            print('Restaurante não encontrado.')
        Modulo.voltar_menu(self)
        return list_


class App(Modulo):
    def __init__(self):
        self.lista_restaurante = (
            {'nome': 'Tavola', 'categoria': 'Pizzaria', 'ativo': False},
            {'nome': 'Sushiman', 'categoria': 'Japonesa', 'ativo': True},)

    def main(self):
        print('''Sabor Express

                1 - Cadastrar restaurante
                2 - Listar restaurante
                3 - Alterar estado do restaurante
                4 - Sair  ''')

        opcao_escolhida = int(input('\nEscolha ma opção: '))
        os.system('cls')
        if opcao_escolhida == 1:
            super().cadastrar_restaurante(self.lista_restaurante)
        elif opcao_escolhida == 2:
            super().listar_restaurante(self.lista_restaurante)
        elif opcao_escolhida == 3:
            super().alterar_estado(self.lista_restaurante)
        elif opcao_escolhida == 4:
            super().finalizar_app()
        else:
            super().opcao_invalida()


if __name__ == '__main__':
    my_app = App()
    my_app.main()
