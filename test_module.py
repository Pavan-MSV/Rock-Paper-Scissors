# test_module.py

import unittest
from RPS_game import play, quincy, mrugesh, kris, abbey
from RPS import player

class UnitTests(unittest.TestCase):
    def test_quincy(self):
        results = play(player, quincy, 1000)
        self.assertGreater(results["player1"], 600, "win rate vs quincy too low")

    def test_abbey(self):
        results = play(player, abbey, 1000)
        self.assertGreater(results["player1"], 600, "win rate vs abbey too low")

    def test_kris(self):
        results = play(player, kris, 1000)
        self.assertGreater(results["player1"], 600, "win rate vs kris too low")

    def test_mrugesh(self):
        results = play(player, mrugesh, 1000)
        self.assertGreater(results["player1"], 600, "win rate vs mrugesh too low")

if __name__ == "__main__":
    unittest.main()
