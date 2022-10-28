from ArrayStack import *

#q1
def stack_sum(s):
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        to_return = val + stack_sum(s)
        s.push(val)
        return to_return

#q2
def eval_prefix(exp_str):
    exp_lst = exp_str.split(" ")
    s = ArrayStack()
    for i in range(len(exp_lst), -1, -1):
        if exp_lst[i].isdigit():
            s.push(int(exp_lst[i]))
        elif exp_lst[i] == "+":
            s.push(s.pop() + s.pop())
        elif exp_lst[i] == "-":
            s.push(s.pop() - s.pop())
        elif exp_lst[i] == "*":
            s.push(s.pop() * s.pop())
        elif exp_lst[i] == "/":
            s.push(s.pop() / s.pop())
    return s.top