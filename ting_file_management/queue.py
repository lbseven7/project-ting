from ting_file_management.abstract_queue import AbstractQueue
# 1 - Implemente uma fila para armazenar os arquivos que serão lidos.


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def search(self, index):
        if index < 0 or index >= len(self.queue):
            raise IndexError()
        else:
            return self.queue[index]
