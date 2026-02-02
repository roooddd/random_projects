import random

def main():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    rodadas = qtd_rodadas()
    pontos_aliados, pontos_inimigos, i = 0, 0, 0

    while i < rodadas:
        try:
            jogada_inimiga, jogada_aliada = jogo(i, opcoes)
            pontos_aliados, pontos_inimigos = soma_pontos(jogada_aliada, jogada_inimiga, pontos_aliados, pontos_inimigos)
            i += 1
        except (TypeError, ValueError):
            print("As jogadas disponíveis são pedra, papel ou tesoura.\n")
            
    
    quem_ganhou(pontos_aliados, pontos_inimigos, opcoes)


def soma_pontos(jogada_aliada, jogada_inimiga, pontos_aliados, pontos_inimigos):    
    # jogador vence
    if jogada_aliada == "Pedra" and jogada_inimiga == "Tesoura" or jogada_aliada == "Tesoura" and jogada_inimiga == "Papel" or jogada_aliada == "Papel" and jogada_inimiga == "Pedra":     
        print("Você ganhou essa rodada!\n")
        pontos_aliados += 1

    # jogador perde
    elif jogada_inimiga == "Pedra" and jogada_aliada == "Tesoura" or jogada_inimiga == "Tesoura" and jogada_aliada == "Papel" or jogada_inimiga == "Papel" and jogada_aliada == "Pedra":
        print("Você perdeu essa rodada!\n")
        pontos_inimigos += 1

    else:
        print("Empate!\n")

    return pontos_aliados, pontos_inimigos

def quem_ganhou(pontos_aliados, pontos_inimigos):
    if pontos_aliados > pontos_inimigos:
        return print(f"====== Você ganhou! ======\n======     {pontos_aliados}x{pontos_inimigos}      ======")
    elif pontos_inimigos > pontos_aliados:
        return print(f"====== Você perdeu... ======\n======      {pontos_inimigos}x{pontos_aliados}       ======")
    else:
        return print(f"====== O jogo empatou! ======\n======      {pontos_inimigos}x{pontos_aliados}       ======")
            
def qtd_rodadas():
    while True:
        try:
            rodadas = int(input("Quantas rodadas deseja jogar? "))
            break
        except ValueError:
            print("A quantidade de rodadas precisa ser um número inteiro!\n")
    return rodadas

def jogo(i, opcoes):
    print(f"====== Partida {i + 1} ======")
    jogada_inimiga =  random.choice(opcoes)
    jogada_aliada = str(input("Pedra... Papel... Tesoura... → ")).title()
    if jogada_aliada not in opcoes:
        return ValueError
    
    print(f"{jogada_aliada} vs {jogada_inimiga}")

    return jogada_inimiga, jogada_aliada

main()
