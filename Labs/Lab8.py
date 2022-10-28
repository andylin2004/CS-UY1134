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
