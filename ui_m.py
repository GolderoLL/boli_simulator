from boli_m import Boli
import time
import sys
import os
from eventos_m import eventos_possiveis
from audio_utils import tocar_som, alternar_som, parar_musica, parar_efeitos

from colorama import init, Fore, Style # type: ignore
init(autoreset=True)

def animar_texto(texto, cor=Fore.WHITE):
    for caractere in texto:
        sys.stdout.write(cor + caractere + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def barra_de_carregamento(segundos=3):
    print(Fore.CYAN + "Rolando o Boli:")
    for i in range(0, 21):
        bar = '#' * i + '-' * (20 - i)
        sys.stdout.write(Fore.GREEN + f"\r[{bar}] {i * 5}%")
        sys.stdout.flush()
        time.sleep(segundos / 20)
    print("\n")

def exibir_titulo():
    print(Fore.WHITE + """
.______     ______    __       __          _______. __  .___  ___.  __    __   __           ___      .___________.  ______   .______      
|   _  \   /  __  \  |  |     |  |        /       ||  | |   \/   | |  |  |  | |  |         /   \     |           | /  __  \  |   _  \     
|  |_)  | |  |  |  | |  |     |  |       |   (----`|  | |  \  /  | |  |  |  | |  |        /  ^  \    `---|  |----`|  |  |  | |  |_)  |    
|   _  <  |  |  |  | |  |     |  |        \   \    |  | |  |\/|  | |  |  |  | |  |       /  /_\  \       |  |     |  |  |  | |      /     
|  |_)  | |  `--'  | |  `----.|  |    .----)   |   |  | |  |  |  | |  `--'  | |  `----. /  _____  \      |  |     |  `--'  | |  |\  \----.
|______/   \______/  |_______||__|    |_______/    |__| |__|  |__|  \______/  |_______|/__/     \__\     |__|      \______/  | _| `._____|
""")
    print(Fore.RED + """
  ____ __       _ _              _       _       __                  
 |__ //  \   __| (_)__ _ ___  __| |___  (_)_ _  / _|___ _ _ _ _  ___ 
  |_ | () | / _` | / _` (_-< / _` / -_) | | ' \|  _/ -_| '_| ' \/ _ \
      
 |___/\__/  \__,_|_\__,_/__/ \__,_\___| |_|_||_|_| \___|_| |_||_\___/
 """)


def exibir_menu():
    print(Fore.YELLOW + "\n=== MENU PRINCIPAL ===")
    print("1. Iniciar Jogo")
    print("2. Créditos")
    print("3. Alternar Som (Ativar/Desativar)")
    print("4. Sair")
    return input(Fore.WHITE + "Escolha uma opção: ")

def intro():
    if input(Fore.WHITE + "Pressione ENTER para continuar ou 's' para pular a introdução: ").lower() == 's':
        return
    else:
        animar_texto("=== INTRODUÇÃO ===", Fore.CYAN)
        animar_texto("Boli vivia sua vida normalmente com seus gloriosos 300kg, até que um dia...", Fore.LIGHTCYAN_EX)
        animar_texto("UM EVENTO INESPERADO ACONTECEU!", Fore.RED )
        animar_texto("SirMod ofereceu para Boli um prêmio de 2 x-burgers se ele conseguisse emagrecer para 80kg em 30 dias!", Fore.LIGHTCYAN_EX)
        animar_texto("Boli aceitou o desafio e agora ele precisa da sua ajuda para emagrecer!", Fore.LIGHTCYAN_EX)
        animar_texto("Você terá 30 dias para ajudá-lo a emagrecer e sobreviver a esse inferno!", Fore.LIGHTCYAN_EX)
        animar_texto("Boa sorte!", Fore.LIGHTRED_EX)
        escolha =  input(Fore.WHITE + "\nPressione ENTER para continuar.")
        if escolha == '':
            animar_texto("=== CARREGANDO JOGO ===", Fore.CYAN )
            barra_de_carregamento()
            animar_texto("Jogo carregado com sucesso!", Fore.GREEN)
            time.sleep(1.5)
            animar_texto("=== INICIANDO JOGO ===", Fore.LIGHTCYAN_EX)
            
    

def exibir_creditos():
    print(Fore.MAGENTA + "\n=== CRÉDITOS ===")
    print("Desenvolvido por: Goldero Informáticas")
    print("Projeto: Boli Simulator - 30 Dias de Inferno")
    input(Fore.WHITE + "\nPressione ENTER para voltar ao menu.")

def mostrar_escolhas(boli):
    print(f"\n Dia {boli.day} de 30 - O que Boli vai fazer hoje?")
    print("1. Fazer exercício")
    print("2. Comer")
    print("3. Dormir")
    print("4. Fazer uma missão")
    print("5. Ir à loja")
    print("6. Usar item do inventário")
    print("7. Alternar som")

    escolha = input("Escolha uma ação (1-6): ")

    if escolha == "1":
        boli.exercitar()
    elif escolha == "2":
        boli.comer()
    elif escolha == "3":
        boli.dormir()
    elif escolha == "4":
        boli.fazer_missao()
    elif escolha == "5":
        from loja_a import abrir_loja
        abrir_loja(boli)
    elif escolha == "6":
        boli.usar_item()
    elif escolha == "7":
        alternar_som()
    else:
        print("Escolha inválida! Tente novamente.")
        return mostrar_escolhas(boli)

def mostrar_status(boli):
    if boli.evento_atual > -1:
        eventoatual = eventos_possiveis(boli.evento_atual)
        print(Fore.GREEN + f"🎉 EVENTO ATUAL: {eventoatual['titulo']}")
        print(Fore.GREEN + eventoatual['descricao'])
        print(Fore.GREEN + '================================= ')
    print(Fore.WHITE + "STATUS DO BOLI:")
    print(f"Peso: ", Fore.RED + f'{boli.peso:.1f} kg')
    print(f"Vibes: ", Fore.BLUE + f'{boli.vibes}/100')
    print(f"Energia: ", Fore.LIGHTMAGENTA_EX + f'{boli.energia}/100')
    print(f"Dinheiro: ", Fore.GREEN + f'R${boli.dinheiro}')
    print(f"Buffs ativos: ", Fore.LIGHTYELLOW_EX + f"{', '.join(boli.buffs.keys()) if boli.buffs else 'Nenhum'}")
    
class Finais:
    def __init__(self):
        pass

    def exibir_final(self, mensagem, ascii_art):
        print(ascii_art)
        animar_texto(mensagem + '\n')
        escolha = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if escolha == 's':
            parar_efeitos()
            from main import main  # importa e chama o main do jogo
            main()
        else:
            print("Saindo do jogo...")
            sys.exit()

    def final_energia(self):
        arte = r"""
        (\__/)
        ( x_x)  Boli morreu de inanição!
        /     \
        """
        mensagem = ("Boli morreu de inanição após VOCÊ deixá-lo sem energia!!!"
                    "\nVocê é um péssimo treinador!"
                    "\nTODOS TE ODEIAM!")
        parar_musica()
        tocar_som('sons/som_final_energia.mp3')
        self.exibir_final(mensagem, arte)

    def final_suicidio(self):
        arte = r"""
        (\__/)
        ( T_T)  Boli não tankou o bostil...
        /     \
        """
        mensagem = ("Boli não conseguiu suportar o peso da sociedade e se suicidou!"
                    "\nVocê é um péssimo treinador!"
                    "\nTODOS TE ODEIAM!")
        parar_musica()
        tocar_som('sons/som_final_suicidio.mp3')
        self.exibir_final(mensagem, arte)

    def final_gnose(self):
        arte = r"""
        🌌  Boli transcendeu 🌌
        """
        mensagem = ("Boli atingiu a Gnose e se livrou das amarras do mundo material e do Demiurgo!"
                    "\nNADA É TUDO!"
                    "\nTUDO É NADA!")
        parar_musica()
        tocar_som('sons/som_final_gnose.mp3')
        self.exibir_final(mensagem, arte)

    def final_feliz(self):
        arte = r"""
        (\^_^/)
        (='.'=)  Boli ATINGIU O IMPOSSÍVEL!!! E agora come seus x-burgers feliz... (oh não, ele está engordando)
        (")_(")
        """
        mensagem = ("Boli conseguiu perder peso e atingiu seu objetivo!!!"
                    "\nVOCÊ É UM ÓTIMO TREINADOR!"
                    "\nTODOS TE AMAM!")
        parar_musica()
        tocar_som('sons/som_final_feliz.mp3')
        self.exibir_final(mensagem, arte)

    def final_30_dias(self):
        arte = r"""
        ( -_-)
        (     )  Boli desistiu...
        """
        mensagem = "Boli não conseguiu emagrecer e desistiu do desafio de 30 dias!"
        parar_musica()
        tocar_som('sons/som_final_30_dias.mp3')
        self.exibir_final(mensagem, arte)