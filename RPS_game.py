# RPS_game.py

import random

def play(player1, player2, num_games, verbose=False):
    player1_prev_play = ""
    player2_prev_play = ""
    player1_opponent_history = []
    player2_opponent_history = []

    results = {"player1": 0, "player2": 0, "tie": 0}

    for _ in range(num_games):
        p1 = player1(player1_prev_play, player1_opponent_history)
        p2 = player2(player2_prev_play, player2_opponent_history)

        if verbose:
            print(f"Player 1: {p1} | Player 2: {p2}")

        if p1 == p2:
            results["tie"] += 1
        elif (p1 == "R" and p2 == "S") or \
             (p1 == "P" and p2 == "R") or \
             (p1 == "S" and p2 == "P"):
            results["player1"] += 1
        else:
            results["player2"] += 1

        player1_prev_play = p2
        player2_prev_play = p1

    return results


def quincy(prev_play, opponent_history=[]):
    # Quincy cycles continuously through a set sequence
    choices = ["R", "P", "S", "R", "P", "S"]
    return choices[len(opponent_history) % len(choices)]


def abbey(prev_play, opponent_history=[]):
    # Abbey copies your move from 2 rounds ago
    if len(opponent_history) > 1:
        return opponent_history[-2]
    return "R"


def kris(prev_play, opponent_history=[]):
    # Kris follows a different repeating pattern
    pattern = ["S", "S", "R", "R", "P", "P"]
    return pattern[len(opponent_history) % len(pattern)]


def mrugesh(prev_play, opponent_history=[]):
    # Mrugesh predicts your next move based on history
    if not opponent_history:
        return "S"

    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == "R":
        return "P"
    if most_frequent == "P":
        return "S"
    return "R"
