from mqt.bench import get_benchmark
from qiskit import QuantumCircuit
from qiskit.transpiler.passes.synthesis import SolovayKitaev
from qiskit.synthesis import generate_basic_approximations
from qiskit.quantum_info import Operator
import qiskit
import os

from utils.file_util import FileUtil
def get_from_qasm(name: str):
    qasm_str = FileUtil.read_all('data' + os.path.sep+'circuits' +os.path.sep+ name)
    circuit = QuantumCircuit.from_qasm_str(qasm_str=qasm_str)
    return circuit
# get a benchmark circuit on algorithmic level representing the GHZ state with 5 qubits
#circuit = get_benchmark(benchmark_name="vqe", level="nativegates", circuit_size=3)

circuit = get_from_qasm('vqe\\vqe_indep_qiskit_3.qasm')

# draw the circuit
circuit.draw('mpl').show()

basis = [ "t", "tdg","x", "z","y","h"]
approx = generate_basic_approximations(basis, depth=3)
skd = SolovayKitaev(recursion_degree=2,basic_approximations=approx)

discretized = skd(circuit)

print("Discretized circuit:")
discretized.draw('mpl').show()