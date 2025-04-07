from boli_m import Boli
from random import choice

class QuestEtapas:
    def __init__(self, descricao, requisito_fn, recompensa_fn=None):
        self.descricao = descricao
        self.requisito_fn = requisito_fn
        self.recompensa_fn = recompensa_fn
        self.completada = False

    def tentar_completar(self, boli):
        if not self.completada and self.requisito_fn(boli):
            self.completada = True
            if self.recompensa_fn:
                self.recompensa_fn(boli)
            return True
        return False

class QuestComplexa:
    def __init__(self, titulo, etapas):
        self.titulo = titulo
        self.etapas = etapas
        self.completada = False

    def progresso(self, boli):
        if self.completada:
            return "Missão concluída."

        for etapa in self.etapas:
            if not etapa.completada:
                if etapa.tentar_completar(boli):
                    print(f"Etapa completada: {etapa.descricao}")
                break  # uma etapa por vez

        if all(e.completada for e in self.etapas):
            self.completada = True
            print(f"Missão COMPLETA: {self.titulo}")
        return self.status()

    def status(self):
        status = f"\n {self.titulo}\n"
        for i, e in enumerate(self.etapas, 1):
            check = "✔️" if e.completada else "🔸"
            status += f"  {check} Etapa {i}: {e.descricao}\n"
        return status

from random import choice

def gerar_quest_emagrecer():
    etapas = [
        QuestEtapas("Perder 5kg", lambda b: b.peso <= 295),
        QuestEtapas("Perder mais 5kg", lambda b: b.peso <= 290),
        QuestEtapas("Chegar a 285kg", lambda b: b.peso <= 285, lambda b: setattr(b, 'vibes', b.vibes + 10))
    ]
    return QuestComplexa("Desafio da Balança", etapas)

def gerar_quest_disciplina():
    etapas = [
        QuestEtapas("Chegar ao dia 2", lambda b: b.day >= 2),
        QuestEtapas("Chegar ao dia 4", lambda b: b.day >= 4),
        QuestEtapas("Chegar ao dia 6", lambda b: b.day >= 6, lambda b: setattr(b, 'dinheiro', b.dinheiro + 20))
    ]
    return QuestComplexa("Rotina de Ferro", etapas)

def gerar_quest_bolympiadas():
    etapas = [
        QuestEtapas("Fazer 2 exercícios seguidos sem dormir", lambda b: b.energia <= 40 and b.day >= 2),
        QuestEtapas("Chegar a 290kg", lambda b: b.peso <= 290),
        QuestEtapas("Fazer mais um exercício com menos de 20 de energia", 
                    lambda b: b.energia <= 20,
                    lambda b: setattr(b, 'vibes', b.vibes + 15))
    ]
    return QuestComplexa("Bolympíadas", etapas)

def gerar_quest_inferno():
    etapas = [
        QuestEtapas("Sobreviver até o dia 10", lambda b: b.day >= 10),
        QuestEtapas("Sobreviver até o dia 20 com mais de 20 de energia", lambda b: b.day >= 20 and b.energia > 20),
        QuestEtapas("Chegar ao dia 30 e estar vivo", 
                    lambda b: b.day >= 30 and b.energia > 0 and b.vibes > 0,
                    lambda b: setattr(b, 'vibes', b.vibes + 50))
    ]
    return QuestComplexa("30 Dias no Inferno", etapas)

def gerar_quest_consumismo():
    etapas = [
        QuestEtapas("Comprar 1 item útil", lambda b: len(b.inventory) >= 1),
        QuestEtapas("Chegar a 3 itens no inventário", lambda b: len(b.inventory) >= 3),
        QuestEtapas("Chegar a 5 itens no inventário", lambda b: len(b.inventory) >= 5,
                    lambda b: setattr(b, 'vibes', b.vibes + 10))
    ]
    return QuestComplexa("Consumismo Controlado", etapas)

def gerar_quest_vibes():
    etapas = [
        QuestEtapas("Alcançar 60 vibes", lambda b: b.vibes >= 60),
        QuestEtapas("Alcançar 75 vibes", lambda b: b.vibes >= 75),
        QuestEtapas("Alcançar 90 vibes", lambda b: b.vibes >= 90,
                    lambda b: setattr(b, 'energia', b.energia + 20))
    ]
    return QuestComplexa("Despertar Espiritual", etapas)

def gerar_quest_mestre_shaboli():
    etapas = [
        QuestEtapas("Acordar com energia cheia (100)", lambda b: b.energia >= 100),
        QuestEtapas("Fazer 3 exercícios em 5 dias", lambda b: b.day >= 5 and b.peso <= 294),
        QuestEtapas("Ficar com energia abaixo de 10 e sobreviver", 
                    lambda b: b.energia <= 10 and b.vibes > 0,
                    lambda b: setattr(b, 'dinheiro', b.dinheiro + 25))
    ]
    return QuestComplexa("O Treinamento do Mestre Sha-Boli", etapas)


def gerar_quest_random():
    return choice([
        gerar_quest_emagrecer(),
        gerar_quest_disciplina(),
        gerar_quest_vibes(),
        gerar_quest_bolympiadas(),
        gerar_quest_consumismo(),
        gerar_quest_inferno(),
        gerar_quest_mestre_shaboli(),
    ])