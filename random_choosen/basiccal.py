import re

class stack():
    def __init__(self):
        self.stack = []
    
    def top(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0

def parse(expression):
    expression = re.sub(r'(\()(\w+)', r'\g<1> \g<2>', expression)
    expression = re.sub(r'(\d+)(\))', r'\g<1> \g<2>', expression)
    for i in range(len(expression)-1):
        if expression[i] == ')' and expression[i+1] == ')':
            expression = expression[:i+1] + ' ' + expression[i+1:]
    return expression.strip().split()

def cal(expression):
    tokens = parse(expression)
    nums =[] 
    for token in tokens:
        if token == ')':
