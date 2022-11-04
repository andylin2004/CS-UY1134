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
    for i in range(len(exp_lst) - 1, -1, -1):
        if exp_lst[i].isdigit():
            s.push(int(exp_lst[i]))
        elif exp_lst[i] == "+":
            s.push(s.pop() + s.pop())
        elif exp_lst[i] == "-":
            s.push(s.pop() - s.pop())
        elif exp_lst[i] == "*":
            s.push(s.pop() * s.pop())
        elif exp_lst[i] == "/":
            s.push(s.pop() // s.pop())
    return s.top()

#q3

def flatten_list(lst):
    """
    : lst type: list
    : return type: None
    """
    for i in range(len(lst) - 1, -1, -1):
        

if __name__ == "__main__":
    s = ArrayStack()
    for i in [1, -14, 5, 6, -7, 9, 10, -5, -8]:
        s.push(i)
    print(stack_sum(s))
    print(eval_prefix("- + * 16 5 * 8 4 20"))
    print(eval_prefix("- * 3 4 10"))
    print(eval_prefix("+ / 10 2 * 5 5"))
    print(eval_prefix("+ 8 / - 10 2 4"))
    print(eval_prefix("+ * 6 3 * 8 4"))
    print(eval_prefix("+ - * 8 2 + 3 6 4 "))
    