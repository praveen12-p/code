import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "R"

    # Build a string of the last 3 opponent moves
    last_moves = "".join(opponent_history[-3:])

    # Search the opponent's history for this pattern
    possible_patterns = {}
    for i in range(len(opponent_history) - 3):
        pattern = "".join(opponent_history[i:i+3])
        next_move = opponent_history[i+3]
        if pattern == last_moves:
            if next_move not in possible_patterns:
                possible_patterns[next_move] = 0
            possible_patterns[next_move] += 1

    # Predict the opponent's next move
    if possible_patterns:
        predicted_move = max(possible_patterns, key=possible_patterns.get)
    else:
        predicted_move = random.choice(["R", "P", "S"])

    # Counter their predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_move]
