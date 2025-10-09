import os
import campeonato1

times = []

def exibir_opcoes_2():
    print('1. Cadastrar Times')
    print('2. Tabela da 1ª Fase')
    print('3. Tabela da 2ª Fase')
    print('4. Lista de Jogos\n')
   
def tabela_quad_final():
    print('bele')

opcoes_camp_2 = {
    1: campeonato1.cadastrar_times,
    2: campeonato1.tabela_pts_corridos,
    3: tabela_quad_final,
    4: campeonato1.lista_de_jogos
}

def menu_camp_2():
    import app
    app.exibir_subtitulo('CAMPEONATO DE PONTOS CORRIDOS + QUADRANGULAR FINAL')
    exibir_opcoes_2()
    app.selecionar_opcao(opcoes_camp_2)