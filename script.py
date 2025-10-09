app fotables
    - criar tabelas para organizar campeonatos de ate 8 times de futebol

funcionalidades
    - cadastrar Time
    # - selecionar regras 
        - 1 fase - pontos corridos
        - 2 fase - pontos corridos + quadrangular final
        - 2 fases - 2 grpos + quadrangular final
    - ver lista de jogos
    - colocoar resultados
    - visualizar grupos
    - visualizar pontos corridos
    - visualizar qudrangular final

1 tela:
    - título
    - breve explicação
    - escolha a regra 

time = jogador + clube 

regra 1
    - cadastrar capitão e time
    - ver tabela do campeonato
    - ver lista de jogos
    - próximo jogo
   

regra 2
    - cadastrar capitão e time
    - 'lista de jogos'
    - 'Tabela 1ª Fase'
    - 'Tabela 2ª Fase'
    - próximo jogo
    

regra 3
    - cadastrar capitão e time
    - lista de jogos
    - 'Tabela Grupo A'
    - 'Tabela Grupo B'
    - 'Tabela 2ª Fase'
    - próximo jogo ---- inserir resultados (talvez)
   
* retornar ao menu do campeonato















 print('1. Cadastrar Time')
    print('2. Tabela do Campeonato')
    print('3. Lista de Jogos')
    print('4. Próximo Jogo\n')



opcao_selecionada_1 = {
    1: 'Cadastrar Time',
    2: 'Tabela do Campeonato'
    3: 'Lista de Jogos'
    4: 'Próximo Jogo\n'
}


def selecionar_opcao(opcoes):
    opcao_escolhida = int(input('\nDigite o número correspondente a opção que deseja selecionar: '))

    funcao = opcoes.get(opcao_escolhida, None)

    if funcao:
        funcao()
    else:
        opcao_invalida()


def selecionar_opcao(opcoes):
    """
    Recebe um dicionário onde:
    - a chave é o número da opção
    - o valor é a função que deve ser executada
    """
    opcao_escolhida = int(input('\nDigite o número da opção desejada: '))

    # Busca a função correspondente no dicionário
    funcao = opcoes.get(opcao_escolhida, None)

    if funcao:
        funcao()  # executa a função associada
    else:
        print("Opção inválida! Tente novamente.")



def ver_cardapio():
    print("🍽️  Exibindo cardápio...")

def fazer_pedido():
    print("🛒  Fazendo pedido...")

def sair():
    print("👋  Saindo...")

opcoes_menu = {
    1: ver_cardapio,
    2: fazer_pedido,
    3: sair
}

selecionar_opcao(opcoes_menu)




def cadastrar_usuario():
    print("👤 Cadastrando usuário...")

def listar_usuarios():
    print("📋 Listando usuários...")

def atualizar_usuario():
    print("✏️ Atualizando usuário...")

def remover_usuario():
    print("❌ Removendo usuário...")

def voltar():
    print("↩️ Voltando ao menu anterior...")

menu_usuarios = {
    1: cadastrar_usuario,
    2: listar_usuarios,
    3: atualizar_usuario,
    4: remover_usuario,
    5: voltar
}

selecionar_opcao(menu_usuarios)