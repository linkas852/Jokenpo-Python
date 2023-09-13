import random
import time

def main():
    print("Olá, bem-vindo ao JoKenPo Master! Seu adversário esta noite será o poderosíssimo 'Seu Jô'.")
    

    while True:
        start = input("Você quer jogar? Se sim, digite 'sim' >:D (Digite 'não' para sair) ").lower()
        print("Para jogar, escolha as seguintes opções: '0' para papel, '1' para pedra, '2' para tesoura e '3' para sair.")
        
        if start != "sim":
            print("Entendido, até a próxima!")
            break

        escolha = int(input("Sua escolha: "))
        maquina = random.randint(0, 2)
        ppt = ['Papel', 'Pedra', 'Tesoura']

        if escolha in [0, 1, 2]:
            print("Jo")
            time.sleep(1)
            print("Ken")
            time.sleep(1)
            print("Po!")
            time.sleep(1)
            print("Seu Jô escolheu {}".format(ppt[maquina]))
            print("Você escolheu {}".format(ppt[escolha]))
            resultado = verificar_vencedor(escolha, maquina)
            print(resultado)
        elif escolha == 3:
            break
        else:
            print("Escolha algo válido (0 para papel, 1 para pedra, 2 para tesoura.)")

def verificar_vencedor(jogador, maquina):
    if jogador == maquina:
        return "Empate"
    elif (jogador == 0 and maquina == 1) or (jogador == 1 and maquina == 2) or (jogador == 2 and maquina == 0):
        return "Você ganhou!"
    else:
        return "Seu Jô ganhou!"

if __name__ == "__main__":
    main()