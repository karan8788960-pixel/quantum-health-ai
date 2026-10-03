from dataclasses import dataclass
from typing import Dict


@dataclass
class QuantumCircuitSpec:
    qubits: int = 4
    depth: int = 3
    shots: int = 1024
    backend: str = "qasm_simulator"
    execution_time_ms: float = 0.0


def create_quantum_circuit(qubits: int = 4) -> QuantumCircuitSpec:
    return QuantumCircuitSpec(qubits=qubits, depth=max(2, qubits // 2), shots=1024, backend="qasm_simulator")


def encode_features(features: Dict[str, float]) -> Dict[str, float]:
    return {k: float(v) for k, v in features.items()}
