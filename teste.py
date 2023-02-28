import random

drawn = random.randint(1, 100)

hit = False

for tent in range(1, 11):
        print(f"Attempt {tent}:", end=" ")
        shot = int(input("Give your shot: "))

        if shot > drawn:
            print("Guess a lower number!")
        elif shot < drawn:
            print("Guess a higher number!")
        else:
           hit = True
           break
if hit:
    print("Congrats, you got it right!")
else:
    print(f"What a pitty, your attempts are over! The number was : {drawn}")