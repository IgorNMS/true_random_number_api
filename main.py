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

@app.get("/numbers/{quantity}/{max_value}")
async def get_multiple_random_numbers(quantity: int, max_value: int):
    random_numbers = []
    try:
        for _ in range(quantity):
            rand_int, _, _ = quantum_rng.return_random_numbers()
            scaled_number = rand_int % max_value
            random_numbers.append(scaled_number)
    except Exception as e:
        return {"error": str(e)}
    else:
        return {
            "random_numbers": random_numbers
        }