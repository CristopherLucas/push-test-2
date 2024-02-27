import os


class Modulo():
    @classmethod
    def finalizar_app(cls):
        print('Encerrando o programa\n')

    @classmethod
    def opcao_invalida(cls, self_):
        input('Você selecinou uma opção inválida. Digite outra tecla para voltar a menu inicial: ')
        os.system('cls')
        App.main(self_)


class App(Modulo):
    def main(self):
        print('''Sabor Favorito
        
                1 - Cadastrar restaurante
                2 - Listar Restaurante
                3 - Ativar Restaurante
                4 - Sair  ''')

        opcao_escolhida = int(input('Escolha ma opção: '))
        os.system('cls')
        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('Listar restaurante')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            Modulo.finalizar_app()
        else:
            Modulo.opcao_invalida(self)


if __name__ == '__main__':
    my_app = App()
    my_app.main()
    print('Olá mundo')
