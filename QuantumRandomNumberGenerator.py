from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from dotenv import load_dotenv
import os

class QuantumRandomNumberGenerator:
    load_dotenv()

    def __init__(self):
        backend_name = os.getenv("BACKEND")
        self.service = QiskitRuntimeService(
            token=os.getenv("TOKEN"),
            instance=os.getenv("INSTANCE"),
            region="us-east",
            channel="ibm_quantum_platform"
        )
        try:
            self.backend = self.service.backend(backend_name)
            self.is_real_hardware = True
            print(f"Connected on quantum backend")
        except:
            print(f"Using simulator backend.")

    def create_random_circuit(self, num_bits=8):
        qc = QuantumCircuit(num_bits, num_bits)
        for i in range(num_bits):
            qc.h(i)

        qc.measure_all()
        return qc
    
    def generate_random_number(self, num_bits=8, shots=1):
        qc = self.create_random_circuit(num_bits)
        transpiled_qc = transpile(qc, self.backend, optimization_level=1)

        sampler = SamplerV2(self.backend)
        job = sampler.run([transpiled_qc], shots=shots)

        print(f"Executing on {self.backend.name}...")

        result = job.result()[0].data
        bitstring = result.meas.get_bitstrings()
        random_number = int(bitstring[0], 2)
        
        return random_number, bitstring

    def generate_random_float(self, num_bits=32):
        max_value = 2**num_bits - 1
        random_int, _ = self.generate_random_number(num_bits)
        return random_int / max_value
    
    def return_random_numbers(self):
        random_int, bits = self.generate_random_number(num_bits=8)
        random_float = self.generate_random_float(num_bits=16)
        return random_int, random_float, bits
