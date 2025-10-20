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
            playlists[nome_playlist].append(musica)
            print(f"Música '{musica[0]}' adicionada à playlist '{nome_playlist}'!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def mostrar_playlists(playlists):
    if not playlists:
        print("Nenhuma playlist criada ainda.")
    else:
        for nome, musicas in playlists.items():
            print(f"\nPlaylist: {nome}")
            if musicas:
                for i, musica in enumerate(musicas, start=1):
                    print(f"  {i}. {musica[0]} - {musica[1]} ({musica[2]} min)")
            else:
                print("  (Vazia)")

def remover_musica(playlists):
    nome_playlist = input("Digite o nome da playlist de onde deseja remover a música: ")
    if nome_playlist not in playlists:
        print("Playlist não encontrada.")
        return
    

def menu():
    while True:
        print("\nMenu de Opções:")
        print("1 - Criar Playlist")
        print("2 - Adicionar Música à Playlist")
        print("3 - Mostrar Playlists")
        print("4 - Mostrar Catálogo")
        print("5 - Sair")
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '1':
            criar_playlist(playlists)
        elif escolha == '2':
            adicionar_musica(playlists)
        elif escolha == '3':
            mostrar_playlists(playlists)
        elif escolha == '4':
            mostrar_catalogo()
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
