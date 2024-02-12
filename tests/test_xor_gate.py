from ..cktos.models.gates import XOR


def test_xor_default_1():
    gate = XOR(2)  # default n_bits is 1
    outputs = []

    gate.change_input(0, 0)
    gate.change_input(1, 0)
    outputs.append(gate()[0])

    gate.change_input(0, 0)
    gate.change_input(1, 1)
    outputs.append(gate()[0])

    gate.change_input(0, 1)
    gate.change_input(1, 0)
    outputs.append(gate()[0])

    gate.change_input(0, 1)
    gate.change_input(1, 1)
    outputs.append(gate()[0])

    gate.inputs = [0, 0]
    outputs.append(gate()[0])

    gate.inputs = [0, 1]
    outputs.append(gate()[0])

    gate.inputs = [1, 0]
    outputs.append(gate()[0])

    gate.inputs = [1, 1]
    outputs.append(gate()[0])

    expected = [0, 1, 1, 0, 0, 1, 1, 0]
    assert outputs == expected, f"Assertion failed with output, expected: {outputs, expected}"


def test_xor_default_2():
    gate = XOR(4)  # default n_bits is 1
    outputs = []

    for i in range(16):
        for j in range(4):
            gate.change_input(j, (i >> j) & 1)
        outputs.append(gate()[0])

    for i in range(16):
        i_bin = format(i, '04b')
        gate.inputs = [int(bit) for bit in i_bin]
        outputs.append(gate()[0])

    expected = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]*2
    assert outputs == expected, f"Assertion failed with output, expected: {outputs, expected}"


def test_xor_3():
    gate = XOR(4, 4, True)
    outputs = []

    gate.change_input(0, 8)
    gate.change_input(1, 11)
    gate.change_input(2, 10)
    gate.change_input(3, 9)
    outputs.append(gate()[0])

    gate.change_input(0, 3)
    gate.change_input(1, 5)
    gate.change_input(2, 0)
    gate.change_input(3, 1)
    outputs.append(gate()[0])

    gate.inputs = [8, 11, 10, 9]
    outputs.append(gate()[0])

    gate.inputs = [3, 5, 0, 1]
    outputs.append(gate()[0])

    expected = [15, 8, 15, 8]
    assert outputs == expected, f"Assertion failed with output, expected: {outputs, expected}"


def test_xor_4():
    gate = XOR(4, 4, False)
    outputs = []

    gate.change_input(0, 8)
    gate.change_input(1, 11)
    gate.change_input(2, 10)
    gate.change_input(3, 9)
    outputs.append(gate()[0])

    gate.change_input(0, 3)
    gate.change_input(1, 5)
    gate.change_input(2, 0)
    gate.change_input(3, 1)
    outputs.append(gate()[0])

    gate.inputs = [8, 11, 10, 9]
    outputs.append(gate()[0])

    gate.inputs = [3, 5, 0, 1]
    outputs.append(gate()[0])

    expected = [0, 7, 0, 7]
    assert outputs == expected, f"Assertion failed with output, expected: {outputs, expected}"
