import notations


def test_1():
    def function1(arg1):
        if arg1:
            return True
        else:
            return False
    assert notations.notation(function1) == notations.NOTATION_TYPES.O_1


def test_2():
    def function2(arg1):
        i = 0
        for a in arg1:
            i += 1
        return i
    assert notations.notation(function2) == notations.NOTATION_TYPES.O_n


def test_3():
    def function3(arg1, arg2):
        i = 0
        j = 0
        for a in arg1:
            for b in arg2:
                i += 1
                j += 1
        return i, j
    assert notations.notation(function3) == notations.NOTATION_TYPES.O_n_power_2


def test_4():
    def function4(arg1, arg2):
        i = 0
        j = 0
        for a in arg1:
            i += 1
        
        for b in arg2:
            j += 1

        return i, j
    assert notations.notation(function4) == notations.NOTATION_TYPES.O_n


def test_5():
    def function5(arg1, arg2):
        pass
    assert notations.notation(function5) == notations.NOTATION_TYPES.O_1


def test_6():
    def function6(arg1):
        i = [a for a in arg1]
        return i

    assert notations.notation(function6, debug=True) == notations.NOTATION_TYPES.O_n


def test_7():
    def function7(arg1):
        i = [a for a in b for b in arg1]
        return i

    assert notations.notation(function7, debug=True) == notations.NOTATION_TYPES.O_n_power_2
