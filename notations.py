import enum
import dis
from collections import deque


FOR_ITER = 'FOR_ITER'
POP_BLOCK = 'POP_BLOCK'


class NOTATION_TYPES(enum.IntEnum):
    O_1 = 0
    O_n = 1
    O_n_power_2 = 2
    O_n_power_n = 3

    def __repr__(self):
        return NOTATION_REPR[self]


NOTATION_REPR = {
    0: 'O(1)',
    1: 'O(n)',
    2: 'O(n^2)',
    3: 'O(n^n)',
}


def notation(func, debug=False):
    bytecode = dis.Bytecode(func)
    max_loop_stack_depth = 0
    # setup the loop stacks as a deque
    loop_stacks = deque()
    for i in bytecode:
        if i.opname == FOR_ITER:
            loop_stacks.append(i.argval)
        elif i.opname == POP_BLOCK:
            offset = loop_stacks.pop()
            if offset != i.offset:  # Check the popped value is the offset of the pop_block
                raise ValueError("Not implemented, maybe. Or maybe this is a bug.")
        else:
            if debug:
                print(i)
        if len(loop_stacks) > max_loop_stack_depth:
            max_loop_stack_depth = len(loop_stacks)

    return NOTATION_TYPES(max_loop_stack_depth)

