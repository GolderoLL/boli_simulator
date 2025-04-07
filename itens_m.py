from typing import Callable, Union
from efeitos_m import efeito_cafe, efeito_trembolona, efeito_monster_branco, efeito_phonk

itens: list[dict[str, Union[str, int, Callable]]] = [
    {
        "nome": "Barra de Proteína",
        "descricao": "Recupera 20 de energia.",
        "preco": 15,
        "efeito": lambda b: setattr(b, "energia", min(b.energia + 20, b.energia_max))
    },
    {
        "nome": "Livro de Autoajuda",
        "descricao": "Aumenta 10 de vibes.",
        "preco": 20,
        "efeito": lambda b: setattr(b, "vibes", min(b.vibes + 10, b.vibes_max))
    },
    {
        "nome": "Suplemento Termogênico",
        "descricao": "Reduz 2kg do peso.",
        "preco": 30,
        "efeito": lambda b: setattr(b, "peso", max(b.peso - 2, 80))
    },
    {
        "nome": "Café",
        "descricao": "Recupera 10 de energia e 5 de vibes.",
        "preco": 5,
        "efeito": efeito_cafe
    },
    {
        "nome": "Trembolona",
        "descricao": "Aumenta 10 de energia, multiplica sua perda de peso por 2.5 durante 3 turnos e reduz 25 de vibes.",
        "preco": 50,
        "efeito": efeito_trembolona
    },
    {
        "nome": "Monster Branco",
        "descricao": "Atividades que aumentam a energia e vibes são multiplicadas por 1.5 durante 3 turnos.",
        "preco": 25,
        "efeito": efeito_monster_branco
    },
    {
        "nome": "Phonk",
        "descricao": "Adiciona mais 0.5 no seu multiplicador de peso (Atividades que diminuem o peso são metade mais efetivas)",
        "preco": 55,
        "efeito": efeito_phonk
    },
]   