import stim
print(stim.__version__)



circuit = stim.Circuit()

# First, the circuit will initialize a Bell pair.
circuit.append("CNOT", [0, 1])

# Then, the circuit will measure both qubits of the Bell pair in the Z basis.
circuit.append("M", [0, 1])

print(circuit.diagram())
print(circuit.diagram('timeslice-svg-html'))

sampler = circuit.compile_sampler()
print(sampler.sample(shots=10))
