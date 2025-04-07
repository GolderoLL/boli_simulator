from gm import Jogo
import time
from ui_m import (
    exibir_titulo,
    exibir_menu,
    exibir_creditos,
    animar_texto,
    barra_de_carregamento,
    intro,
)
from audio_utils import alternar_som, tocar_musica

def main():
    while True:
        exibir_titulo()
        tocar_musica('sons/musica_fundo.mp3')
        opcao = exibir_menu()

        if opcao == "1":    
            intro()
            jogo = Jogo()
            jogo.jogar()

        elif opcao == "2":
            exibir_creditos()

        elif opcao == "3":
            alternar_som()

        elif opcao == "4":
            animar_texto("Saindo do jogo. Boli permanecerá gordo eternamente!\n")
            break

        else:
            animar_texto("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()