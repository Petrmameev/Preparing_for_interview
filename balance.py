from stack import Stack

def object(string):
    open_object = ['(', '{', '[']
    closing_object = [')', '}', ']']
    stack = Stack()

    if len(string) % 2 > 0:
        return ('Несбалансированный')

    for a, b in enumerate(string):
        if b in open_object:
            stack.push(b)
        elif b in closing_object:
            if stack.is_empty():
                return ('Несбалансированный')
            elif open_object.index(stack.peek()) != closing_object.index(b):
                return ('Несбалансированный')
            else:
                stack.pop()
                if stack.is_empty() and a == len(string) - 1:
                    return ('Сбалансированный')

if __name__ == '__main__':
    print(object(input('Введите выражение: ')))

