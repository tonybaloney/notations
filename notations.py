import ast
import inspect
import dis
from collections import deque

FOR_ITER = 'FOR_ITER'
POP_BLOCK = 'POP_BLOCK'

O_n = 'O(n)'
O_n_power_2 = 'O(n^2)'
O_n_power_n = 'O(n^n)'

NOTATIONS = {
    0: O_n,
    1: O_n_power_2,
    2: O_n_power_n,
    # etc..
}


def function1(arg1):
    if arg1 == True:
        return True
    else:
        return False


def function2(arg1):
    i = 0
    for a in arg1:
        i += 1
    return i


def function3(arg1, arg2):
    i = 0
    j = 0
    for a in arg1:
        for b in arg2:
            i += 1
            j += 1
    return i, j


def function4(arg1, arg2):
    i = 0
    j = 0
    for a in arg1:
        i += 1
    
    for b in arg2:
        j += 1

    return i, j


def function5(arg1, arg2):
    pass

def notation(func):
    bytecode = dis.Bytecode(func)
    max_loop_stack_depth = 0
    # setup the loop stacks as a deque
    loop_stacks = deque()
    for i in bytecode:
        if i.opname == FOR_ITER:
            loop_stacks.append(i.argval)
        if i.opname == POP_BLOCK:
            offset = loop_stacks.pop()
            if offset != i.offset:  # Check the popped value is the offset of the pop_block
                raise ValueError
        if len(loop_stacks) > max_loop_stack_depth:
            max_loop_stack_depth = len(loop_stacks)

    # For now, just return the max stack depth
    return NOTATIONS[max_loop_stack_depth]

print("Function 1 has a loop stack of ", notation(function1))
print("Function 2 has a loop stack of ", notation(function2))
print("Function 3 has a loop stack of ", notation(function3))
print("Function 4 has a loop stack of ", notation(function4))
print("Function 5 has a loop stack of ", notation(function5))