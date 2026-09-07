game_finished = False

while not game_finished:
    print("The game is running...")

    answer = input("Did you win? (yes/no): ")

    if answer == "yes":
        game_finished = True

print("Game Over!")