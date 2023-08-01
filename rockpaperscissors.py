import random

def get_user_input():
  """Gets the user's input of rock, paper, or scissors."""
  while True:
    user_input = input("Enter rock, paper, or scissors: ").lower()
    if user_input in ["rock", "paper", "scissors"]:
      return user_input
    else:
      print("Invalid input. Please enter rock, paper, or scissors.")

def get_computer_input():
  """Gets the computer's random input of rock, paper, or scissors."""
  return random.choice(["rock", "paper", "scissors"])

def get_winner(user_input, computer_input):
  """Returns the winner of the game."""
  if user_input == computer_input:
    return "Draw"
  elif user_input == "rock":
    return "Player 1 wins" if computer_input == "scissors" else "Automated robot wins"
  elif user_input == "paper":
    return "Player 1 wins" if computer_input == "rock" else "Automated robot wins"
  else:
    return "Player 1 wins" if computer_input == "paper" else "Automated robot wins"

def main():
  """Plays a game of Rock Paper Scissors against the computer."""
  user_input = get_user_input()
  computer_input = get_computer_input()
  winner = get_winner(user_input, computer_input)
  print(f"Winner: {winner}")

  # Append the result of the game to the rps file.
  with open("rps", "a") as f:
    f.write(f"{winner}, {user_input}, {computer_input}\n")

if __name__ == "__main__":
  main()






