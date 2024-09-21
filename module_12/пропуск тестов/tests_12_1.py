import runner
import unittest
import functools

def skip_if_frozen(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args and hasattr(args[0], 'is_frozen') and args[0].is_frozen:
            print("Тесты в этом кейсе заморожены")
            return unittest.skip("Тесты в этом кейсе заморожены")
        return func(*args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        my_runner = runner.Runner("test1")

        for i in range(10):
            my_runner.walk()
        self.assertEqual(my_runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        my_runner2 = runner.Runner("test2")

        for i in range(10):
            my_runner2.run()
        self.assertEqual(my_runner2.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        my_runner3 = runner.Runner("test3")
        my_runner4 = runner.Runner("test4")

        for i in range(10):
            my_runner3.run()
            my_runner4.walk()
        self.assertNotEqual(my_runner3.distance, my_runner4.distance)
