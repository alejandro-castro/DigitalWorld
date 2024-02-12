from ..cktos.models.gates import NOT, AND, OR, XOR


def test_not_default():
    gate = NOT()  # default n_bits is 1
    gate.change_input(0, 1)
    output1 = gate()[0]

    gate.change_input(0, 0)
    output2 = gate()[0]

    gate.inputs = [0]
    output3 = gate()[0]

    gate.inputs = [1]
    output4 = gate()[0]

    assert (output1 == 0) and (output2 == 1) and (output3 == 1) and (output4 == 0), \
        f"Assertion failed with output, expected: {output1, 0, output2, 1, output3, 1, output4, 0}"


def test_not_1():
    gate = NOT(4)
    gate.change_input(0, 13)
    output1 = gate()[0]

    gate.change_input(0, 3)
    output2 = gate()[0]

    gate.inputs = [13]
    output3 = gate()[0]

    gate.inputs = [3]
    output4 = gate()[0]

    assert (output1 == 2) and (output2 == 12) and (output3 == 2) and (output4 == 12), \
        f"Assertion failed with output, expected: {output1, 2, output2, 12, output3, 2, output4, 12}"


def test_not_2():
    gate = NOT(32)
    gate.change_input(0, -1)
    output1 = gate()[0]

    gate.change_input(0, -100)
    output2 = gate()[0]

    gate.inputs = [-1]
    output3 = gate()[0]

    gate.inputs = [-100]
    output4 = gate()[0]

    assert (output1 == 0) and (output2 == 99) and (output3 == 0) and (output4 == 99), \
        f"Assertion failed with output, expected: {output1, 0, output2, 99, output3, 0, output4, 99}"

