import time
from audio_utils import tocar_som
from colorama import Fore

class Boli:
    def __init__(self):
        self.peso = 300 # em kilograma
        self.energia = 100 
        self.energia_max = 100
        self.vibes = 50
        self.vibes_max = 100
        self.vibes_min = 0
        self.inventory = []
        self.inventory_max = 10
        self.day = 1
        self.dinheiro = 50
        self.multiplicador_peso = 1.0
        self.multiplicador_vibes = 1.0  
        self.multiplicador_energia = 1.0
        self.multiplicador_dinheiro = 1.0
        self.buffs = {}
        self.missao = None
        self.checar_loop = 0
        self.evento_atual = -1
    
    def aplicar_buff(self, nome, duracao):
        self.buffs[nome] = duracao
        if nome == "trembolona":
            self.multiplicador_peso += 2.5
        elif nome == "monster_branco":
            self.multiplicador_energia *= 1.5
            self.multiplicador_vibes *= 1.5
        elif nome == 'palestra':
            self.multiplicador_peso += 1.5
    
    def atualizar_buffs(self):
        buffs_para_remover = []
        for buff in self.buffs:
            self.buffs[buff] -= 1
            if self.buffs[buff] <= 0:
                buffs_para_remover.append(buff)
        for buff in buffs_para_remover:
            del self.buffs[buff]
            if buff == "trembolona":
                self.multiplicador_peso -= 2.5
                print("O efeito da Trembolona passou! FAKE NATTY!")
            elif buff == "monster_branco":
                self.multiplicador_energia /= 1.5
                self.multiplicador_vibes /= 1.5
                print("O efeito do Monster Branco passou! Denied access to Agartha!")
    
    def exercitar(self):
        self.peso -= 8 * self.multiplicador_peso
        self.energia -= 30 * self.multiplicador_energia
        self.vibes -= 5 * self.multiplicador_vibes
        self.day += 1
        self.checar_loop = 0
        tocar_som('sons/som_exercicio.mp3')
        self.atualizar_buffs()

    def comer(self):
        self.peso += 1 / self.multiplicador_peso
        if self.energia <= 80:
            self.energia += 20 / self.multiplicador_energia 
        self.vibes += 10 / self.multiplicador_vibes
        self.day += 1
        self.checar_loop = 0
        tocar_som('sons/som_comer.mp3')
        self.atualizar_buffs()

    def dormir(self):
        if self.energia <= 60:
            self.energia += 40
        self.vibes += 2
        self.day += 1
        tocar_som('sons/som_dormir.mp3')
        self.checar_loop = 0
        self.atualizar_buffs()
    
    def fazer_missao(self):
        if not self.missao:
            print("Você ainda não tem uma missão ativa.")
            aceitar = input("Deseja iniciar uma missão aleatória? (s/n): ").lower()
            if aceitar == 's':
                from quests_a import gerar_quest_random
                self.missao = gerar_quest_random()
                print(f"Nova missão: {self.missao.titulo}")
            else:
                print("Missão ignorada.")
                return
        print(self.missao.progresso(self))
    
    def usar_item(self):
        if not self.inventory:
            print("Seu inventário está vazio.")
            time.sleep(1.5)
            return
        print(Fore.YELLOW + "I N V E N T Á R I O:")
        for i, item in enumerate(self.inventory):
            print(Fore.LIGHTBLACK_EX + f"{i+1}. ",Fore.RED + f"{item['nome']} - ",Fore.LIGHTGREEN_EX + f"{item['descricao']}")
        escolha = input("Escolha um item para usar (ou 0 para voltar): ")
        
        if escolha == "0":
            return
        try:
            item = self.inventory.pop(int(escolha)-1)
            item["efeito"](self)
            print(Fore.RED + f"Você usou {item['nome']}")
        except (IndexError, ValueError):
            print("Escolha inválida.")