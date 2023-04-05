class Stack:
    def __init__(self):
        self.stack = []

    # Проверка стека на пустоту. Метод возвращает True или False
    def is_empty(self):
        return len(self.stack) == 0

    # Добавляет новый элемент на вершину стека. Метод ничего не возвращает
    def push(self, new_element):
        self.stack.append(new_element)

    # Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        return self.stack.pop()

    # Возвращает верхний элемент стека, но не удаляет его. Стек не меняется
    def peek(self):
        return self.stack[-1]

    # Возвращает количество элементов в стеке
    def size(self):
        return len(self.stack)

