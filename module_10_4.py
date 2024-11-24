import queue
import threading

from queue import Queue
import random
lock = threading.Lock

import time

class Table():
    def __init__(self, number = 1):
        self.number = number # number of table
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name, ):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        rand = random.randint(3, 10)
        print(self.name)
        time.sleep(rand)

class Cafe():
    def __init__(self, *table):
        self.queue = Queue()
        self.tables = [t for t in table]


    def guest_arrival(self, *guests):
        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    seated = True
                    break
            if not seated:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла).')
                    print(f'Стол номер {table.number} свободен.')
                    table.guest = None
                if not self.queue.empty():
                    table.guest =  self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()






