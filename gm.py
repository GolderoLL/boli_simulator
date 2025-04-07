from boli_m import Boli
from ui_m import Finais, mostrar_escolhas, mostrar_status, clear_terminal
from eventos_m import evento_diario
from quests_a import gerar_quest_random


class Jogo:
    def __init__(self):
        self.boli = Boli()
        self.finais = Finais()  
        self.quest_ativa = gerar_quest_random()


    def jogar(self):
        while True:
            clear_terminal()
            print(self.quest_ativa.progresso(self.boli))
            fim = self.checar_finais()
            if fim:
                break
            mostrar_status(self.boli)
            evento_diario(self.boli)
            mostrar_escolhas(self.boli)
            self.boli.checar_loop += 1
            
            

    def checar_finais(self):
        if self.boli.energia <= 0:
            self.finais.final_energia()
            return True
        elif self.boli.vibes <= 0:
            self.finais.final_suicidio()
            return True
        elif self.boli.vibes >= self.boli.vibes_max:
            self.finais.final_gnose()
            return True
        elif self.boli.peso <= 80:
            self.finais.final_feliz()
            return True
        elif self.boli.day >= 30:
            self.finais.final_30_dias()
            return True
        return None