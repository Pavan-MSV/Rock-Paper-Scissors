# main.py

from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player
import pytest

if __name__ == "__main__":
    print("\nTesting your player against bots:\n")

    print("Vs Quincy:")
    print(play(player, quincy, 1000))

    print("\nVs Abbey:")
    print(play(player, abbey, 1000))

    print("\nVs Kris:")
    print(play(player, kris, 1000))

    print("\nVs Mrugesh:")
    print(play(player, mrugesh, 1000))

    # Uncomment this to run unit tests
    # pytest.main()
