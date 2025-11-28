# RPS.py

# Example (starter) player. Replace it with your own strategy.
# You will paste your advanced player() function here.

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    guess = "R"
    return guess
