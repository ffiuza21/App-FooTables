import os

times = []

def exibir_opcoes_1():
    print('1. Cadastrar Times')
    print('2. Tabela do Campeonato')
    print('3. Lista de Jogos\n')

def cadastrar_times():
    import app

    if len(times) <= 7:
        while len(times) <= 7:
            app.exibir_subtitulo('Cadastro de Times')
            clube = input('Digite o nome do clube: ')
            capitao = input('Digite o nome do capitão do time: ')
            time = {'capitao': capitao, 'clube': clube}
            times.append(time)
            print(f'\nO clube {clube} do capitão {capitao} foi registrado com sucesso')
            input('Digite uma tecla para cadastrar o próximo time: ')
        
        print('\nO limite máximo de clubes registrados foi atingido')
        app.retornar_menu(menu_camp_1)
         # refatorar para consguir mudar para outro menus

    else:
        app.exibir_subtitulo('Cadastro de Times')
        print('O campeonato já atingiu seu limite de 8 times registrados')
        app.retornar_menu(menu_camp_1) 
        # refatorar para consguir mudar para outro menus
    
def tabela_pts_corridos():
    import app
    app.exibir_subtitulo('Tabela do Campeonato')







def lista_de_jogos():
    print('bele')

opcoes_camp_1 = {
    1: cadastrar_times,
    2: tabela_pts_corridos,
    3: lista_de_jogos,
}

def menu_camp_1():
    import app
    app.exibir_subtitulo('CAMPEONATO DE PONTOS CORRIDOS')
    exibir_opcoes_1()
    app.selecionar_opcao(opcoes_camp_1, menu_camp_1)