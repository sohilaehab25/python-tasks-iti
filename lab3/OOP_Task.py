from asyncio import queues
from operator import imod
import pickle
import json


class Queue1:

    def __init__(self):
        self.queue = []
        
    def insert(self, value):
        self.queue.append(value)

    def is_empty(self):
        return len(self.queue) == 0

    def pop(self):
        if self.is_empty():
            print('Invalid instruction, trying to remove value from an empty queue!')
            return
        return self.queue.pop(0)

    def print(self):
        print(self.queue)


class QueueOutOfRangeException(Exception):
    pass


class Queue2(Queue1):

    instances = dict()

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size

        Queue2.instances[self.name] = self.__dict__

    def insert(self, value):
        if len(self.queue) >= self.size:
            raise QueueOutOfRangeException(f'The max values to store in this queue is {self.size} and try to store more values.')
        else:
            super().insert(value)

    
    def save(self):
        queues = Queue2.load()
        print(queues)
        queues = list(queues)
        queues.append(self.__dict__)
        with open('Instances.json', 'w') as file:
            json.dump(queues, file)

    @classmethod
    def load(cls):
        try:
            with open('Instances.json', 'r') as file:
                loaded_instances = json.load(file)
                return loaded_instances
        except FileNotFoundError:
            return [] 


qq = Queue2('num1', 1)
qq.insert(4)

q2 = Queue2('num2', 2)
q2 = Queue2('num3', 3)
q2 = Queue2('num4', 4)
q2 = Queue2('num5', 5)
qq.save()
q2.save()
r = Queue2.load()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(r)
