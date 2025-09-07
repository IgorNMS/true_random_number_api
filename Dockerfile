FROM python:3.9
ADD main.py .
ADD QuantumRandomNumberGenerator.py .
RUN pip install qiskit qiskit-ibm-runtime "fastapi[standard]" fastapi python-dotenv
CMD ["fastapi", "run", "./main.py", "--port", "8080"]