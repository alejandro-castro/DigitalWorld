import math
from base import CombinationalCkto


class HalfAdder(CombinationalCkto):
    def __init__(self):
        # The half adder has only two 1-bit inputs
        # It doesn't have sense to have the negate option
        super().__init__(2, 1, negate=False)

    def update(self):
        out = self.inputs[0] + self.inputs[1]
        self.outputs = [out % 2, out // 2]  # Output, carry


class FullAdder(CombinationalCkto):
    def __init__(self):
        # The full adder has only three 1-bit inputs
        # It doesn't have sense to have the negate option
        super().__init__(3, 1, negate=False)

    def update(self):
        out = self.inputs[0] + self.inputs[1] + self.inputs[2]
        self.outputs = [out % 2, out // 2]  # Output, carry


class Mux(CombinationalCkto):
    def __init__(self, n_inputs, n_bits=1):
        # It doesn't have sense to have the negate option
        # The last input should be the select
        # The first input correspond to select equals to 0
        assert math.log(n_inputs - 1, 2).is_integer()
        super().__init__(n_inputs, n_bits, negate=False)

    def update(self):
        selector = self.inputs[-1]
        self.outputs = [self.inputs[selector]]

    # Maybe we need to override the getter of the property n_inputs, to assert the property


class Demux(CombinationalCkto):
    def __init__(self, n_outputs, n_bits=1):
        # It doesn't have sense to have the negate option
        # The last input should be the select
        # The output 0 correspond to select equals to 0
        assert math.log(n_outputs, 2).is_integer()
        super().__init__(2, n_bits, negate=False)

        self.n_outputs = n_outputs

    @property
    def n_outputs(self):
        return self._n_outputs

    @n_outputs.setter
    def n_outputs(self, value):
        self._n_outputs = value
        self.outputs = [0] * value

    def update(self):
        selector = self.inputs[-1]

        self.outputs = [0]*self.n_outputs
        self.outputs[selector] = self.inputs[0]


class CodWithPriority(CombinationalCkto):
    def __init__(self, n_bits=2):
        # It doesn't have sense to have the negate option
        # To match the usual use of the cod, there is going to be only with input with n_bits width
        assert math.log(n_bits, 2).is_integer()
        super().__init__(1, n_bits, negate=False)

    def update(self):
        # Aux is used to get the index search from the MSBs
        i = self.n_bits - 1
        bit = 1
        while bit and (i >= 0):
            bit = (self.inputs[0] >> i) & 1
            i -= 1

        self.outputs = [i + 1]
        # If no input bit is one then the output is set to zero


class Decod(CombinationalCkto):
    def __init__(self, n_bits):
        # It doesn't have sense to have the negate option
        # To match the usual use of the cod, there is going to be only with input with n_bits width
        super().__init__(1, n_bits, negate=False)

    def update(self):
        self.outputs = [2 ** self.inputs[0]]
