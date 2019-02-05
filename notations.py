"""
Notations

Estimate the notation for a given Python function by exploring loop nesting. 
"""

__version__ = '0.1.0'

import ast
import inspect
import enum
import dis
from collections import deque
import types


FOR_ITER = 'FOR_ITER'
POP_BLOCK = 'POP_BLOCK'
LOAD_CONST = 'LOAD_CONST'
MAKE_FUNCTION = 'MAKE_FUNCTION'


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
    """
    Get the Big-O notation for a Python code object.

    :param func: The code object to analyse
    :type  func: ``types.CodeType``

    :param debug: Show debug information
    :type  debug: ``bool``

    :return: Return the O-notation for a given code object
    :rtype: :class:`NOTATION_TYPES`
    """
    if debug:
        print(dis.code_info(func))
    bytecode = dis.Bytecode(func)
    _nested_func = None  # Nested functions, e.g. lambdas and comprehensions
    max_loop_stack_depth = 0
    extra_stacks = 0
    # setup the loop stacks as a deque
    loop_stacks = deque()
    for i in bytecode:
        if i.opname == FOR_ITER:  # basic for loop
            loop_stacks.append(i.argval)
        elif i.opname == LOAD_CONST and isinstance(i.argval, types.CodeType):
            # Load code objects onto the stacks, evaluate the notation of the object
            # and store locally if that function is loaded.
            _nested_notation = notation(i.argval, debug=debug)
        elif i.opname == MAKE_FUNCTION:
            # Where there is a dynamically-generated function, add the loop-stack-depth of it.
            if _nested_func:
                extra_stacks += int(_nested_func)
        elif i.opname == POP_BLOCK:  # pop back up the stack.
            offset = loop_stacks.pop()
            if offset != i.offset:  # Check the popped value is the offset of the pop_block
                raise ValueError("Not implemented, maybe. Or maybe this is a bug.")
        else:
            if debug:
                print(i)
        if len(loop_stacks) > max_loop_stack_depth:
            max_loop_stack_depth = len(loop_stacks)

    return NOTATION_TYPES(max_loop_stack_depth + extra_stacks)

