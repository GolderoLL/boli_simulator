import os
import pygame
from colorama import Fore

pygame.mixer.init()

# Canais específicos: 0 = efeitos, 1 = trilha sonora
canal_efeitos = pygame.mixer.Channel(0)
canal_musica = pygame.mixer.Channel(1)

# Flags de ativação
efeitos_ativados = True
musica_ativada = True

def tocar_som(nome_arquivo):
    if not efeitos_ativados:
        return

    caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
    if not os.path.exists(caminho):
        print(Fore.YELLOW + f"[AVISO] Efeito não encontrado: {caminho}")
        return
    try:
        som = pygame.mixer.Sound(caminho)
        canal_efeitos.play(som)
    except Exception as e:
        print(Fore.YELLOW + f"[AVISO] Não foi possível tocar o efeito: {e}")

def tocar_musica(nome_arquivo, loop=True):
    if not musica_ativada:
        return

    caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
    if not os.path.exists(caminho):
        print(Fore.YELLOW + f"[AVISO] Música não encontrada: {caminho}")
        return
    try:
        musica = pygame.mixer.Sound(caminho)
        canal_musica.play(musica, loops=-1 if loop else 0)
    except Exception as e:
        print(Fore.YELLOW + f"[AVISO] Não foi possível tocar a música: {e}")

def parar_musica():
    canal_musica.stop()

def parar_efeitos():
    canal_efeitos.stop()

def alternar_som():
    from ui_m import animar_texto
    global efeitos_ativados, musica_ativada

    animar_texto("Qual som deseja alternar?", cor=Fore.YELLOW)
    animar_texto("1. Efeitos\n2. Música\n3. Ambos", cor=Fore.YELLOW)
    escolha = input("> ").strip()

    if escolha == "1":
        efeitos_ativados = not efeitos_ativados
        estado = "ativados" if efeitos_ativados else "desativados"
        animar_texto(f"Efeitos sonoros {estado}.", cor=Fore.YELLOW)
        if efeitos_ativados:
            tocar_som('sons/som_ativar.mp3')

    elif escolha == "2":
        musica_ativada = not musica_ativada
        estado = "ativada" if musica_ativada else "desativada"
        animar_texto(f"Música {estado}.", cor=Fore.YELLOW)
        if musica_ativada:
            tocar_som('sons/som_ativar.mp3')
        if not musica_ativada:
            parar_musica()

    elif escolha == "3":
        efeitos_ativados = not efeitos_ativados
        musica_ativada = not musica_ativada
        estado = "ativados" if efeitos_ativados and musica_ativada else "desativados"
        animar_texto(f"Som {estado}.", cor=Fore.YELLOW)
        if efeitos_ativados or musica_ativada:
            tocar_som('sons/som_ativar.mp3')
        if not musica_ativada:
            parar_musica()
    else:
        animar_texto("Opção inválida.", cor=Fore.YELLOW)