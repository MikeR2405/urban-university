import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        my_runner = runner.Runner("test1")

        for i in range(10):
            my_runner.walk()
        self.assertEqual(my_runner.distance, 50)

    def test_run(self):
        my_runner2 = runner.Runner("test2")

        for i in range(10):
            my_runner2.run()
        self.assertEqual(my_runner2.distance, 100)

    def test_challenge(self):
        my_runner3 = runner.Runner("test3")
        my_runner4 = runner.Runner("test4")

        for i in range(10):
            my_runner3.run()
            my_runner4.walk()
        self.assertNotEqual(my_runner3.distance, my_runner4.distance)