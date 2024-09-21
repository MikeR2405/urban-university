import runner
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.R1 = runner.Runner("Усэйн", 10)
        self.R2 = runner.Runner("Андрей", 9)
        self.R3 = runner.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("Результаты:")
        for place, runner in cls.all_results.items():
            print(f'| {place} место - {runner.name} - {runner.distance}')
        print()

    def test_Usein_and_Nik(self):
        tournament = runner.Tournament(90)
        tournament.participants = [self.R1, self.R3]
        all_results = tournament.start()
        self.all_results.update(all_results)
        last_runner = max(self.all_results.values(), key=lambda x: x.distance)
        self.assertTrue(last_runner in [self.R1, self.R3])

    def test_Andrey_and_Nik(self):
        tournament = runner.Tournament(90)
        tournament.participants = [self.R2, self.R3]
        all_results = tournament.start()
        self.all_results.update(all_results)
        last_runner = max(self.all_results.values(), key=lambda x: x.distance)
        self.assertTrue(last_runner in [self.R2, self.R3])

    def test_Usein_Andrey_and_Nik(self):
        tournament = runner.Tournament(90)
        tournament.participants = [self.R1, self.R2, self.R3]
        all_results = tournament.start()
        self.all_results.update(all_results)
        last_runner = max(self.all_results.values(), key=lambda x: x.distance)
        self.assertTrue(last_runner in [self.R1, self.R2, self.R3])

    def test_runner_finishes_race(self):
        tournament = runner.Tournament(10)
        tournament.participants = [self.R1]
        all_results = tournament.start()
        self.assertEqual(len(all_results), 1)
        self.assertEqual(all_results[1], self.R1)

    def test_runner_does_not_finish_race(self):
        tournament = runner.Tournament(100)
        tournament.participants = [self.R3]
        all_results = tournament.start()
        self.assertEqual(len(all_results), 0)

if __name__ == '__main__':
    unittest.main()
