# Create a mapping dictionary
player_to_opponent = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

# Get the player and find the opponent
player = input("Enter a player (A, B, or C): ")
opponent = player_to_opponent.get(player, "Unknown")

print(f"The opponent of player {player} is {opponent}.")
