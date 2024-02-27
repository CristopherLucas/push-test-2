import os

class Modulo():
    def __init__(self, self_) -> None:
        self.self_ = self_

    def finalizar_app(self):
        print('Encerrando o programa\n')

    def opcao_invalida(self):
        input('\nVocê selecinou uma opção inválida. Digite outra tecla para voltar a menu inicial: ')
        os.system('cls')
        self.self_.App.main()

    def voltar_menu(self):
        input('\nDigite uma tecla para voltar a menu inicial: ')
        os.system('cls')
        self.self_.App.main()

    def cadastrar_restaurante(self, list_:list):
        os.system('cls')
        nome_restaurante = input('''Cadastro de Restaurantes

Insira o nome do restaurante que deseja cadastrar: ''').title()
        list_.append({'nome': nome_restaurante, 'ativo': False})
        print(f'O restaurente {nome_restaurante} foi adicionado.')
        Modulo.voltar_menu(self.self_)
        return list_

    def listar_restaurante(self, list_:list):
        for restaurante in list_:
            nome_restaurante = restaurante['nome']
            if restaurante['ativo']:
                print(f'{nome_restaurante} - O restaurante está ativo.')
            else:
                print(f'{nome_restaurante} - O restaurante está inativo.')
        Modulo.voltar_menu(self.self_)

class App():
    def __init__(self, modulo) -> None:
        self.modulo = modulo(self)
        self.restaurantes = list()
    def main(self):
        while True:
            try:
                print('''Sabor Express
            
    1 - Cadastrar restaurante
    2 - Listar Restaurante
    3 - Ativar Restaurante
    4 - Sair  ''')

                opcao_escolhida = int(input('Esolha uma opção: '))
                os.system('cls')
                if opcao_escolhida == 1:
                    self.restaurantes = self.modulo.cadastrar_restaurante(self.restaurantes)
                elif opcao_escolhida == 2:
                    self.modulo.listar_restaurante(self.restaurantes)
                elif opcao_escolhida == 3:
                    print('Ativar restaurante')
                elif opcao_escolhida == 4:
                    self.modulo.finalizar_app()
                    break
                else:
                    self.modulo.opcao_invalida()
            except ValueError:
                self.modulo.opcao_invalida()

if __name__ == '__main__':
    my_app = App(Modulo)
    my_app.main()
