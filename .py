catalogo = [
    ("Máquina do Tempo", "Matuê", 3.50),
    ("Conexões de Máfia", "Matuê, Rich The Kid", 3.42),
    ("Imagina esse Cenário", "Matuê, Veigh", 2.35),
    ("A Morte do Autotune", "Matuê", 3.37),
    ("Talvez você precise de mim", "Veigh, Supernova Ent", 2.07),
    ("Visões", "Veigh, Supernova Ent", 2.47),
    ("Cartas na Mesa (Bônus)", "Kayblack, Wall Hein", 2.25),
    ("Eu Sei Bem", "Kayblack, Wall Hein", 2.33),
    ("Te Devo Nada", "BK, FYE, JXNV$, Nansy Silvvz", 4.25),
    ("Tá Tarde", "Vulgo FK, BK, Murillo e LT no Beat, Fepache", 3.20),
    ("Cacos de Vidro (sample: Esperar para Ver)", "BK, Kolo, Evinha", 2.29),
    ("Minha Vida é um Filme", "Teto", 3.06),
    ("Vidigal", "WIU", 3.17),
    ("Horas Iguais", "WIU, Oruam", 4.06),
    ("Coração de Gelo", "WIU", 2.48),
    ("Tenho Que Me Decidir", "MC PH. Borges, WIU, Pedro Lotto, WEY", 3.51)
]

playlists = {}

def mostrar_catalogo():
    print("\nCatálogo de Músicas:")
    for i, musica in enumerate(catalogo, start=1):
        titulo, artista, tempo = musica
        print(f"{i} - {titulo} - {artista} ({tempo} min)")

def criar_playlist(playlists):
    nome_playlist = input("Digite o nome da playlist: ")
    if nome_playlist in playlists:
        print("Já existe uma playlist com esse nome.")
    else:
        playlists[nome_playlist] = []
        print(f"Playlist '{nome_playlist}' criada com sucesso!")

def adicionar_musica(playlists):
    nome_playlist = input("Digite o nome da playlist onde deseja adicionar a música: ")
    if nome_playlist not in playlists:
        print("Playlist não encontrada.")
        return
    mostrar_catalogo()
    try:
        numero_musica = int(input("Digite o número da música que deseja adicionar: "))
        if 1 <= numero_musica <= len(catalogo):
            musica = catalogo[numero_musica - 1]
            if musica in playlists[nome_playlist]:
                print("Essa música já está na playlist")
                return
            playlists[nome_playlist].append(musica)
            print(f"Música '{musica[0]}' adicionada à playlist '{nome_playlist}'!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def remover_musica(playlists):
    nome_playlist = input("Digite o nome da playlist de onde deseja remover a música: ")
    if nome_playlist not in playlists:
        print("Playlist não encontrada.")
        return
    titulo= input("Digite o título da música que deseja remover: ")
    for musica in playlists[nome_playlist]:
        if musica[0].lower() == titulo.lower():
            playlists[nome_playlist].remove(musica)
            print(f"Música '{titulo}' removida da playlist '{nome_playlist}'!")
            return
    
def mostrar_playlists(playlists):
    nome = input("Digite o nome da playlist que deseja ver: ")
    if nome not in playlists:
        print("Playlist não encontrada.")
        return  
    elif not playlists[nome]:
        print("A playlist está vazia.")
    else:
        print(f"\n Musicas na playlist '{nome}':")
        for musica in playlists[nome]:
            print(f"- {musica[0]} - {musica[1]} ({musica[2]} min)")

def estatisticas_playlist(playlists):
        nome = input("Digite o nome da playlist para ver as estatísticas: ")
        if nome not in playlists:
            print("Playlist não encontrada.")
            return
        musicas = playlists[nome]
        if not musicas:
            print("A playlist está vazia.")
            return
        
        total_playlists = len(playlists)
        total_musicas = len(musicas)
        duracao_total = sum(musica[2] for musica in musicas)
        musica_mais_longa = max(musicas)
        titulo_mais_longo = musica_mais_longa[0]
        duracao_mais_longa = musica_mais_longa[2]
        
        print(f"\nEstatísticas da playlist '{nome}':")
        print(f"Total de playlists já criadas: {total_playlists}")
        print(f"Total de músicas: {total_musicas}")
        print(f"Duração total: {duracao_total:.2f} min")
        print(f"Música mais longa: {titulo_mais_longo}, {duracao_mais_longa}min")

def buscar_musica_por_palavra_chave():
    palavra_chave = input("Digite a palavra-chave para buscar na música: ").lower()
    resultados = []

    for titulo, artista, tempo in catalogo:
        if palavra_chave in titulo.lower() or palavra_chave in artista.lower():
            resultados.append((titulo, artista, tempo))

    if resultados:
        print("\nMúsicas encontradas:")
        for titulo, artista, tempo in resultados:
            print(f"- {titulo} - {artista} ({tempo} min)")
    else:
        print("Nenhuma música encontrada com essa palavra-chave.")

def menu():
    while True:
        print("\nMenu de Opções:")
        print("[1] - Criar Playlist")
        print("[2] - Adicionar Música à Playlist")
        print("[3] - Listar Músicas adicionadas na Playlist")
        print("[4] - Mostrar Catálogo")
        print("[5] - Buscar Músicas por palavra-chave")
        print("[6] - Remover Música da Playlist")
        print("[7] - Estatísticas da Playlist")
        print("[8] - Sair")
        escolha = input("Escolha uma opção [1]-[8]: ")

        if escolha == '1':
            criar_playlist(playlists)
        elif escolha == '2':
            adicionar_musica(playlists)
        elif escolha == '3':
            mostrar_playlists(playlists)
        elif escolha == '4':
            mostrar_catalogo()
        elif escolha == '5':
            buscar_musica_por_palavra_chave()
        elif escolha == '6':
            remover_musica(playlists)
        elif escolha == '7':
            estatisticas_playlist(playlists)
        elif escolha == '8':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
