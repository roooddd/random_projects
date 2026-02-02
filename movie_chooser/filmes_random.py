import random

with open("filmes.txt", "r", encoding="utf-8") as lista:
    filmes = [linha.strip() for linha in lista if linha.strip()]

while True:
    filme_escolhido = random.choice(filmes)
    print(f"\n---------------------------------\nFILME SORTEADO:\n-> {filme_escolhido}\n---------------------------------")
    
    while True:
        escolha = str(input("\nDeseja sortear novamente (s/n)? ")).lower()
        if escolha == 's':
            break
        elif escolha == 'n':
            exit()
        else:
            print("\n>>>ERRO<<<\n> Escolha entre 's' para SIM e 'n' para NÃO <")
            