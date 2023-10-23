import random
numeroc = random.randint(0,5)
numerou = int(input("adivinhe o numero que o computador escolheu de 0 a 5!"))
if numerou == numeroc:
    print(f"você acertou era {numeroc}")
else: 
    print (f"você errou, o numero era {numeroc}")