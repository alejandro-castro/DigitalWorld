# Combinational Abstractions, the n_bits is only use for purpose of showing the outputs and change the view
# Because inside the class works with 32 bits for each input to calculate the output
class CombinationalCkto(object):
    def __init__(self, n_inputs, n_bits, negate=False):
        self.inputs = None
        self.output = 0

        self.n_bits = n_bits
        self.n_inputs = n_inputs
        self.negate = negate

    def update(self):
        pass

    @property
    def n_inputs(self):
        return self._n_inputs

    @n_inputs.setter
    def n_inputs(self, value):
        self._n_inputs = value
        self.inputs = [0]*self._n_inputs

    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, value):
        assert (value is None) or (len(value) == self.n_inputs)
        self._inputs = value

    def change_input(self, position, new):
        # It doesn't update automatically so more changes it can be made before actually computing the output
        self.inputs[position] = new

    def __call__(self):
        self.update()
        return self.output  # It is a list
