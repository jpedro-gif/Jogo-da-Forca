import random


palavras = ["gato", "cachorro", "casa", "computador", "elefante",
             "janela", "carro", "livro", "mochila", "telefone"]

def escolher_palavra():
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_certas):
    resultado = ""
    for letra in palavra:
        if letra in letras_certas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jogar():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 6

    print("=== JOGO DA FORCA ===")
    print(f"A palavra tem {len(palavra)} letras\n")

    while tentativas > 0:
        print(mostrar_palavra(palavra, letras_certas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}\n")

        
        if all(letra in letras_certas for letra in palavra):
            print(f"🎉 Parabéns! Você acertou a palavra: {palavra}")
            return

        chute = input("Digite uma letra: ").lower()

        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas uma letra!\n")
            continue

        if chute in letras_certas or chute in letras_erradas:
            print("Você já tentou essa letra!\n")
            continue

        if chute in palavra:
            letras_certas.append(chute)
            print("✅ Letra certa!\n")
        else:
            letras_erradas.append(chute)
            tentativas -= 1
            print("❌ Letra errada!\n")

    print(f"💀 Game over! A palavra era: {palavra}")


jogar()