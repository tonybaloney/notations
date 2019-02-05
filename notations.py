"""
Notations

Estimate the notation for a given Python function by exploring loop nesting. 
"""

__version__ = '0.1.0'

import ast
import inspect
import dis
from collections import deque


FOR_ITER = 'FOR_ITER'
POP_BLOCK = 'POP_BLOCK'

class NOTATION_TYPES:
    O_1 = 'O(1)'
    O_n = 'O(n)'
    O_n_power_2 = 'O(n^2)'
    O_n_power_n = 'O(n^n)'

NOTATIONS = {
    0: NOTATION_TYPES.O_1,
    1: NOTATION_TYPES.O_n,
    2: NOTATION_TYPES.O_n_power_2,
    3: NOTATION_TYPES.O_n_power_n,
    # etc..
}


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

