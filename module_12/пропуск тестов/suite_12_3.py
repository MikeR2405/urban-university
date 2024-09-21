import unittest
from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
