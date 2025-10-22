import os
import random
import pandas as pd
import numpy as np

times = []

def exibir_opcoes_1():
    print('1. Cadastrar Times')
    print('2. Tabela do Campeonato')
    print('3. Lista de Jogos\n')

def cadastrar_times():
    import app
    app.exibir_subtitulo('Cadastro de Times')

    if len(times) < 8:
        while len(times) < 8:
            app.exibir_subtitulo('Cadastro de Times')
            clube = input('Digite o nome do clube: ')
            capitao = input('Digite o nome do capitão do time: ')
            time = {'capitao': capitao, 'clube': clube}
            times.append(time)
            print(f'\nO clube {clube} do capitão {capitao} foi registrado com sucesso')
            input('Confirme para cadastrar o próximo time: ')
        
        app.exibir_subtitulo('Cadastro de Times')
        print('\nO limite máximo de clubes registrados foi atingido')
        app.retornar_menu(menu_camp_1)
        

    else:
        app.exibir_subtitulo('Cadastro de Times')
        print('O campeonato já atingiu seu limite de 8 times registrados')
        app.retornar_menu(menu_camp_1) 
        
    
def tabela_pts_corridos():
    import app
    app.exibir_subtitulo('Tabela do Campeonato')

    if len(times) == 0:
        print('Não há times cadastrados')
        app.retornar_menu(menu_camp_1)

    df = pd.DataFrame(times)
    df['Pontos'] = 0
    df['Jogos'] = 0
    df['Vitórias'] = 0
    df['Empates'] = 0
    df['Derrotas'] = 0
    df['GM'] = 0
    df['GC'] = 0
    df['Saldo'] = df['GM'] - df['GC']

    print(df)
    app.retornar_menu(menu_camp_1)
    







def lista_de_jogos():
    import app
    app.exibir_subtitulo('Lista de Jogos')
    if len(times) == 8:
        time_aleatorio = random.choice(times)
        print(time_aleatorio['clube'])


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