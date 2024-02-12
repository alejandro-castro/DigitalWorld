from ..cktos.models.gates import AND


def test_and_default_1():
    gate = AND(2)  # default n_bits is 1
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

    expected = [0, 0, 0, 1, 0, 0, 0, 1]
    assert outputs == expected, f"Assertion failed with output, expected: {outputs, expected}"


def test_and_default_2():
    gate = AND(4)  # default n_bits is 1
    outputs = []

    for i in range(16):
        for j in range(4):
            gate.change_input(j, (i >> j) & 1)
        outputs.append(gate()[0])

    for i in range(16):
        i_bin = format(i, '04b')
        gate.inputs = [int(bit) for bit in i_bin]
        outputs.append(gate()[0])

    expected = [0] * 15 + [1] + [0] * 15 + [1]
    assert outputs == expected, f"Assertion failed with output, expected: {outputs, expected}"


def test_and_3():
    gate = AND(4, 4, True)
    outputs = []

    gate.change_input(0, 15)
    gate.change_input(1, 11)
    gate.change_input(2, 10)
    gate.change_input(3, 14)
    outputs.append(gate()[0])

    gate.change_input(0, 3)
    gate.change_input(1, 5)
    gate.change_input(2, 11)
    gate.change_input(3, 15)
    outputs.append(gate()[0])

    gate.inputs = [15, 11, 10, 14]
    outputs.append(gate()[0])

    gate.inputs = [3, 5, 11, 15]
    outputs.append(gate()[0])

    expected = [5, 14, 5, 14]
    assert outputs == expected, f"Assertion failed with output, expected: {outputs, expected}"


def test_and_4():
    gate = AND(4, 4, False)
    outputs = []

    gate.change_input(0, 15)
    gate.change_input(1, 11)
    gate.change_input(2, 10)
    gate.change_input(3, 14)
    outputs.append(gate()[0])

    gate.change_input(0, 3)
    gate.change_input(1, 5)
    gate.change_input(2, 11)
    gate.change_input(3, 15)
    outputs.append(gate()[0])

    gate.inputs = [15, 11, 10, 14]
    outputs.append(gate()[0])

    gate.inputs = [3, 5, 11, 15]
    outputs.append(gate()[0])

    expected = [10, 1, 10, 1]
    assert outputs == expected, f"Assertion failed with output, expected: {outputs, expected}"
