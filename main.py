from fastapi import FastAPI
from QuantumRandomNumberGenerator import QuantumRandomNumberGenerator

app = FastAPI(title="True Random Number API", version="0.0.1")
quantum_rng = QuantumRandomNumberGenerator()

@app.get("/")
async def get_random_number():
    try:
        random_int, random_float, bits = quantum_rng.return_random_numbers()
    except Exception as e:
        return {"error": str(e)}
    else:
        return {
            "random_integer": random_int,
            "random_float": random_float,
            "bitstring": bits
        }