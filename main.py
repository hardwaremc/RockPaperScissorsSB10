import random

def rock_paper_scissors():
  user = input("Escolha pedra, papel ou tesoura: ")
  computer = random.choice(['pedra', 'papel', 'tesoura'])
  print(f"JoséBot escolheu {computer}")

  if user == computer:
    return "Empate!"

  elif (user == "pedra" and computer == "tesoura" or (user == "papel" and computer == "pedra")) or (user == "tesoura" and computer == "papel"):
    return "Você ganhou!"
  else:
    return "Você perdeu!"

print(rock_paper_scissors())
