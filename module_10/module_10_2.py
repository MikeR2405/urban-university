import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power, condition, shared_day):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.condition = condition
        self.shared_day = shared_day

    def run(self):
        print(f"{self.name}, на нас напали!")
        start_time = time.time()
        for day in range(1, 11):
            with self.condition:
                while day > self.shared_day[0]:
                    self.condition.wait()

                self.enemies -= self.power
                elapsed_time = time.time() - start_time
                print(f"{self.name} сражается {day} день(дня)..., осталось {self.enemies} воинов.")
                time.sleep(1)

                if self.enemies <= 0:
                    print(f"{self.name} одержал победу спустя {day} день(дня)!")
                    break

                self.shared_day[0] += 1
                self.condition.notify_all()

        print(f"{self.name}: все битвы закончились!")


def main():
    condition = threading.Condition()
    shared_day = [1]

    knights = [Knight("Sir Lancelot", 10, condition, shared_day),
               Knight("Sir Galahad", 20, condition, shared_day)]

    for knight in knights:
        knight.start()

    while any(knight.is_alive() for knight in knights):
        time.sleep(1)


if __name__ == "__main__":
    main()
