import os

class Modulo():
    @classmethod
    def finalizar_app(cls):
        print('Encerrando o programa\n')

    @classmethod
    def opcao_invalida(cls, self_):
        input('\nVocê selecinou uma opção inválida. Digite outra tecla para voltar a menu inicial: ')
        os.system('cls')
        App.main(self_)

    @classmethod
    def voltar_menu(cls, self_):
        input('\nDigite uma tecla para voltar a menu inicial: ')
        os.system('cls')
        App.main(self_)

    @classmethod
    def cadastrar_restaurante(cls, list_:list, self_):
        os.system('cls')
        nome_restaurante = input('''Cadastro de Restaurantes

Insira o nome do restaurante que deseja cadastrar: ''').title()
        list_.append({'nome': nome_restaurante, 'ativo': False})
        print(f'O restaurente {nome_restaurante} foi adicionado.')
        Modulo.voltar_menu(self_)
        return list_

    @classmethod
    def listar_restaurante(cls, list_:list, self_):
        for restaurante in list_:
            nome_restaurante = restaurante['nome']
            if restaurante['ativo']:
                print(f'{nome_restaurante} - O restaurante está ativo.')
            else:
                print(f'{nome_restaurante} - O restaurante está inativo.')
        Modulo.voltar_menu(self_)

class App(Modulo):
    def __init__(self) -> None:
        super().__init__()
        self.restaurantes = list()
    def main(self):
        try:
            print('''Sabor Express
            
    1 - Cadastrar restaurante
    2 - Listar Restaurante
    3 - Ativar Restaurante
    4 - Sair  ''')

            opcao_escolhida = int(input('Esolha uma opção: '))
            os.system('cls')
            if opcao_escolhida == 1:
                self.restaurantes = Modulo.cadastrar_restaurante(self.restaurantes, self)
            elif opcao_escolhida == 2:
                Modulo.listar_restaurante(self.restaurantes, self)
            elif opcao_escolhida == 3:
                print('Ativar restaurante')
            elif opcao_escolhida == 4:
                Modulo.finalizar_app()
                return False
            else:
                Modulo.opcao_invalida(self)
        except ValueError:
            Modulo.opcao_invalida(self)

if __name__ == '__main__':
    my_app = App()
    INICIALIZADO = True
    while INICIALIZADO:
        INICIALIZADO = my_app.main()
