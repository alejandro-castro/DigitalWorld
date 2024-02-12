# Combinational Abstractions, the n_bits is only use for purpose of showing the outputs and change the view
# Because inside the class works with 32 bits for each input to calculate the output
class CombinationalCkto(object):
    def __init__(self, n_inputs, n_bits, negate=False):
        self.n_bits = n_bits
        self.inputs = None
        self.n_inputs = n_inputs
        self.negate = negate

        self.outputs = [0]  # We set outputs after n_bits is set

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
        if value:
            self._inputs = [e & int(f"0b{'1'*self.n_bits}", 2) for e in value]

    def change_input(self, position, new):
        # It doesn't update automatically so more changes it can be made before actually computing the output
        self.inputs[position] = new & int(f"0b{'1'*self.n_bits}", 2)

    @property
    def outputs(self):
        return self._outputs

    @outputs.setter
    def outputs(self, value):
        self._outputs = [e & int(f"0b{'1'*self.n_bits}", 2) for e in value]

    def __call__(self):
        self.update()
        return self.outputs  # It is a list
