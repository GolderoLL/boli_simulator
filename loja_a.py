from itens_m import itens
from boli_m import Boli
from colorama import Fore
import time
from audio_utils import tocar_som

def abrir_loja(boli):
    print("\n LOJA DE ITENS:")
    for i, item in enumerate(itens):
        print(Fore.RED + (f"{i+1}. "), Fore.WHITE + f"{item['nome']} - ", Fore.GREEN + f"R${item['preco']}")
        print(Fore.BLUE + f"   {item['descricao']}")

    print(f"\n Seu dinheiro: ", Fore.GREEN + f"R${boli.dinheiro}")
    escolha = input("Digite o número do item que deseja comprar (ou 0 para sair): ")

    if escolha == "0":
        return
    try:
        item = itens[int(escolha)-1]
        if boli.dinheiro >= item["preco"]:
            if len(boli.inventory) >= boli.inventory_max:
                print("🎒 Inventário cheio!")
                return
            boli.dinheiro -= item["preco"]
            boli.inventory.append(item)
            tocar_som('sons/som_compra.mp3')
            print(f"Você comprou: {item['nome']}")
            time.sleep(1)
        else:
            tocar_som('sons/som_sem_dindin.mp3')
            print("Você não tem dinheiro suficiente.")
            time.sleep(1)
    except (IndexError, ValueError):
        print("Escolha inválida.")