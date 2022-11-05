from ArrayStack import *

running = True
variables = {}

while running:
    num_stack = ArrayStack()
    var_name_to_save = ''
    equation_parts = input("--> ").split()
    if len(equation_parts) == 1 and equation_parts[0] == "done()":
        running = False
    else:
        for i in equation_parts:
            if i == '+':
                num_stack.push(num_stack.pop() + num_stack.pop())
            elif i == '-':
                num_stack.push(- num_stack.pop() + num_stack.pop())
            elif i == '*':
                num_stack.push(num_stack.pop() * num_stack.pop())
            elif i == '/':
                num_stack.push(1 / num_stack.pop() * num_stack.pop())
            elif i == '=':
                var_name_to_save = equation_parts[0]
            elif i.isnumeric():
                num_stack.push(int(i))
            else:
                if i in variables:
                    print(variables)
                    num_stack.push(variables[i])
        if var_name_to_save == '':
            print(num_stack.pop())
        else:
            variables[var_name_to_save] = num_stack.pop()
            print(var_name_to_save)
    