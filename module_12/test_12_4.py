import logging
import unittest
import runner
import os

log_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'runner_tests.log')

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            R1 = runner.Runner(name='Вас', speed=-1)
            logging.info('"Тест test_walk выполнен успешно"')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            R2 = runner.Runner(name='Иллья')
            logging.info('"Тест test_run выполнен успешно"')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    logging.basicConfig(
        filename=log_file_path,  # Use the log_file_path variable
        filemode='w',
        encoding='UTF-8',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )
    unittest.main()
    logging.shutdown()
