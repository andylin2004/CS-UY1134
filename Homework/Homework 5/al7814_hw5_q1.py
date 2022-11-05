from ArrayStack import *

running = True
variables = {}

while running:
    num_stack = ArrayStack()
    var_name_to_save = ''
    equation_parts = input("--> ").split()
    for i in equation_parts:
        if i == '+':
            num_stack.push(num_stack.pop() + num_stack.pop())
        elif i == '-':
            num_stack.push(num_stack.pop() - num_stack.pop())
        elif i == '*':
            num_stack.push(num_stack.pop() * num_stack.pop())
        elif i == '/':
            num_stack.push(num_stack.pop() / num_stack.pop())
        elif i == '=':
            var_name_to_save = equation_parts[0]
        elif i.isnumeric():
            num_stack.push(int(i))
    