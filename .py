catalogo = [("Máquina do Tempo","Matuê", 3.50),
            ("Conexões de Máfia", "Matuê,Rich The Kid", 3.42),
            ("Imagina esse Cenário", "Matuê, Veigh", 2.35),
            ("A Morte do Autotune", "Matuê", 3.37),
            ("Talvez você precise de mim", "Veigh, Supernova Ent", 2.07),
            ("Visões", "Veigh, Supernova Ent", 2.47),
            ("Cartas na Mesa(Bônus)", "Kayblack, Wall Hein", 2.25),
            ("Eu Sei Bem", "Kayblack, Wall Hein", 2.33),
            ("Te Devo Nada", "BK, FYE, JXNV$, Nansy Silvvz", 4.25),
            ("Ta Tarde", "Vulgo FK, BK, Murillo e LT no Beat, Fepache", 3.20),
            ("Cacos De Vidro(sample: Esperar para Ver)", "BK, Kolo, Evinha", 2.29),
            ("Minha Vida é Um Filme", "Teto", 3.06),
            ("Vidigal", "WIU", 3.17),
            ("Horas Iguais", "WIU, Oruam", 4.06),
            ("Coração de Gelo", "WIU", 2.48),
            ("Tenho Que Me Decidir", "MC PH. Borges, WIU, Pedro Lotto, WEY", 3.51),  
            ]

def mostrar_musicas():
    print("Catálogo de Músicas: ")
    numero = 1
    for musica in catalogo:
        titulo = musica[0]
        artista = musica[1]
        tempo = musica[2]
        print(numero, "-", titulo, "-", artista, "(", tempo, "min)")
        numero += 1
mostrar_musicas()