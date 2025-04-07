from audio_utils import tocar_som

def efeito_cafe(boli):
    """Recupera 10 de energia e 5 de vibes."""
    boli.energia = min(boli.energia + 10, boli.energia_max)
    boli.vibes = min(boli.vibes + 5, boli.vibes_max)
    tocar_som('sons/som_cafe.mp3')
    print("Uma vez disse Albert Camus: Entre o café e a morte, a escolha é o absurdo.")

def efeito_trembolona(boli):
    """Aumenta 10 de energia, multiplica sua perda de peso por 2.5 durante 3 turnos e reduz 25 de vibes."""
    boli.aplicar_buff("trembolona", 3)
    boli.energia = min(boli.energia + 10, boli.energia_max)
    boli.vibes = max(boli.vibes - 25, boli.vibes_min)
    tocar_som('sons/som_trembolona.mp3')
    print("Você tomou Trembolona! ESSE É O SUCO!!!")

def efeito_monster_branco(boli):
    """Atividades que aumentam a energia e vibes são multiplicadas por 1.5 durante 3 turnos."""
    boli.aplicar_buff("monster_branco", 3)
    tocar_som('sons/som_monster.mp3')
    print("Você tomou Monster Branco! Yup, anotha Agartha classic!")

def efeito_phonk(boli):
    """Adiciona mais 0.5 no seu multiplicador de peso (Atividades que diminuem o peso são metade mais efetivas)"""
    boli.multiplicador_peso += 0.5
    tocar_som('sons/som_phonk.mp3')
    print("NORTH MEMPHIS BITCH! Boli se sente motivado e agora perde peso mais rápido!")

def efeito_assalto(boli):
    boli.dinheiro -= 30
    boli.vibes -= 10
    tocar_som('sons/som_assalto.mp3')

def efeito_palestra(boli):
    boli.aplicar_buff("palestra", 2)
    tocar_som('sons/som_palestra.mp3') 