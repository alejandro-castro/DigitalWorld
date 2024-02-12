from base import CombinationalCkto


class NOT(CombinationalCkto):
    def __init__(self, n_inputs, n_bits=1):
        super().__init__(n_inputs, n_bits, negate=False)

    def update(self):
        self.output = ~self.inputs


class AND(CombinationalCkto):
    def __init__(self, n_inputs, n_bits=1, negate=False):
        super().__init__(n_inputs, n_bits, negate)

    def update(self):
        out = -1
        for i in range(self.n_inputs):
            out = out & self.inputs[i]

        self.output = ~out if self.negate else out


class OR(CombinationalCkto):
    def __init__(self, n_inputs, n_bits=1, negate=False):
        super().__init__(n_inputs, n_bits, negate)

    def update(self):
        out = 0
        for i in range(self.n_inputs):
            out = out | self.inputs[i]

        self.output = ~out if self.negate else out


class XOR(CombinationalCkto):
    def __init__(self, n_inputs, n_bits=1, negate=False):
        super().__init__(n_inputs, n_bits, negate)

    def update(self):
        out = 0
        for i in range(self.n_inputs):
            out = out ^ self.inputs[i]

        self.output = ~out if self.negate else out
