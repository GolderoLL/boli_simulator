import random
from boli_m import Boli
from efeitos_m import efeito_assalto, efeito_palestra
from typing import Union, Callable
from colorama import Fore
from audio_utils import tocar_som


agartha: list[dict[str, Union[str, int, Callable]]] = [
        {
            "titulo": "Flamengo perdeu!",
            "descricao": "Hoje o mengão perdeu! Boli ficou triste e depressivo perdendo 20 de vibes.",
            "efeito": lambda b: setattr(b, "vibes", max(b.vibes - 20, b.vibes_min))
        },
        {
            "titulo": "Mengão ganhou!",
            "descricao": "Hoje o mengão ganhou! Boli ficou feliz e ganhou 20 de vibes.",
            "efeito": lambda b: setattr(b, "vibes", min(b.vibes + 20, b.vibes_max))
        },
        {
            "titulo": "Conversa com o Goldero",
            "descricao": "Boli teve uma conversa com o Goldero sobre as intrincidades da existência e ganhou 10 de vibes.",
            "efeito": lambda b: setattr(b, "vibes", min(b.vibes + 10, b.vibes_max))
        },
        {
            "titulo": "Assalto na rua!",
            "descricao": "Um velho leproso assaltou o Boli! Ele perdeu 30 reais e 10 de vibes!",
            "efeito": efeito_assalto
        },
        {
            "titulo": "Palestra do Pablo Marçal",
            "descricao": "Boli assistiu uma palestra do Pablo Marçal e está absurdamente motivado! 1.5x de perda de peso durante 2 turnos!",
            "efeito": efeito_palestra
        },
        {
            "titulo": "Dinheiro dos pais",
            "descricao": "O Boli(herdeiro) recebeu 55 reais de mesada dos pais!",
            "efeito": lambda b: setattr(b, "dinheiro", b.dinheiro + 55)
        },
        {
            "titulo": "Gelo da gatinha",
            "descricao": "Tomou gelo da gatinha no Whatsapp! Perdeu 15 de vibes!",
            "efeito": lambda b: setattr(b, "vibes", max(b.vibes - 15, b.vibes_min))
        },
        {
            "titulo": "Reunião da staff",
            "descricao": "Boli teve uma reunião da staff pudimversal e teve que escutar o Jony falar por 2 horas, -20 de vibes!",
            "efeito": lambda b: setattr(b, "vibes", max(b.vibes - 20, b.vibes_min))
        }
    ]

def eventos_possiveis(atual):
    if atual == 69:
        return agartha
    else:
        return agartha[atual]

def evento_diario(boli):
    chance = 0.3  # 30% de chance pra alguma retardadice acontecer
    if random.random() < chance:
        eventos_com_possibilidade = eventos_possiveis(69)
        if boli.checar_loop == 1:
            evento = random.randint(0, len(eventos_com_possibilidade) - 1)
            from ui_m import animar_texto
            tocar_som('sons/som_evento.mp3')
            animar_texto(f"\n🎉 PRÓXIMO EVENTO: {eventos_possiveis(evento)['titulo']}", Fore.RED)
            print(Fore.LIGHTRED_EX + f"{eventos_possiveis(evento)['descricao']}")
            eventos_possiveis(evento)['efeito'](boli)
            boli.evento_atual = evento
    else:
        print("Nada de especial aconteceu hoje.")