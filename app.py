import os
import campeonato1
import campeonato2
# import campeonato3

def exibir_nome_do_app():
    print('''
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████─██████████████─██████████████─██████████████───██████─────────██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██████░░██─██████░░██████─██░░██████░░██─██░░██████░░██───██░░██─────────██░░██████████─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░██──██░░██─██░░██──██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██████████─██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░██████░░██─██░░██████░░████─██░░██─────────██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░██████░░██─██░░████████░░██─██░░██─────────██░░██████████─██████████░░██─
─██░░██─────────██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░██──██░░██─██░░██────██░░██─██░░██─────────██░░██─────────────────██░░██─
─██░░██─────────██░░██████░░██─██░░██████░░██─────██░░██─────██░░██──██░░██─██░░████████░░██─██░░██████████─██░░██████████─██████████░░██─
─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████─────────██████████████─██████████████─────██████─────██████──██████─████████████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

modelos_de_campeonato = {
    1: campeonato1.menu_camp_1,
    2: campeonato2.menu_camp_2,  
    # 3: 
}

def exibir_modelos_campeonato():
    print('1. Somente Pontos Corridos')
    print('2. Pontos Corridos + Quadragular Final')
    print('3. Fases de Grupos + Quadrangular Final')

def opcao_invalida(menu_funcao):
    print('A opção selecionada é inválida')
    retornar_menu(menu_funcao)

def selecionar_opcao(campeonato, menu_funcao):
    opcao_escolhida = int(input('\nDigite e confirme o número correspondente a opção que deseja selecionar: '))

    funcao = campeonato.get(opcao_escolhida, None)

    if funcao: # se a função for true, ou seja encontrada, executa função
        funcao()
    else:
        opcao_invalida(menu_funcao)

def retornar_menu(menu_funcao):
    input('\nConfirme uma tecla para retornar ao menu princiapl: ')
    menu_funcao()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '=' * (len(subtitulo))
    print(linha)
    print(subtitulo)
    print(linha)
    print()

def main():
    os.system('cls')
    exibir_nome_do_app()
    print('O FooTables é um app que permite organizar seus campeonatos de futebol para 8 times')
    print('Escolha qual regra abaixo será utilizada em seu campeonato\n')
    exibir_modelos_campeonato()
    selecionar_opcao(modelos_de_campeonato, main)

if __name__ == '__main__': # Indicando programa como principal
    main()

