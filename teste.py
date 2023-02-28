import random

sorteado = random.randint(1, 101)

acertou = False

for tent in range(1, 11):
        print(f"{sorteado}")
        print(f"Tentativa {tent}:", end=" ")
        chute = int(input("Digite o chute: "))

        if chute > sorteado:
            print("Tente um número mais baixo!")
        elif chute < sorteado:
            print("Tente um número mais alto")
        else:
           acertou = True
           break
if acertou:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena, suas tentativas acabaram! O número era: {sorteado}")