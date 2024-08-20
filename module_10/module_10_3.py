import random
import threading
import time

class Bank:
    lock = threading.Lock()
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)

            with self.lock:
                self.balance += amount
                print(f'Пополнение: {amount}, баланс: {self.balance}')

                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                    continue

            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')

            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонён, недостаточно средств')

                    self.lock.acquire()

            time.sleep(0.001)

if __name__=='__main__':
    bk = Bank(100)

    t1 = threading.Thread(target=bk.deposit)
    t2 = threading.Thread(target=bk.take)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'Итоговый баланс: {bk.balance}')