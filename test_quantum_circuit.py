#imports
from qiskit import QuantumCircuit
import quantum_circuit as q_c

def test_normalization_2qubit_1():
    assert q_c.normalize_inputs([1, 1, 1, 1]) == [0.5+0.j, 0.5+0.j, 0.5+0.j, 0.5+0.j]

def test_normalization_2qubit_2():
    assert q_c.normalize_inputs([0, 1, 0, 0]) == [0+0.j, 1+0.j, 0+0.j, 0+0.j]

def test_normalization_2qubit_3():
    assert q_c.normalize_inputs([1.2, 1.5, 1j, 0]) == [0.5541085158475322+0j, 0.6926356448094152+0j, 0.+0.4617570965396101j, 0. +0.j]

def test_normalization_2qubit_1len():
    assert len(q_c.normalize_inputs([1, 1, 1, 1])) == 4

def test_normalization_2qubit_2len():
    assert len(q_c.normalize_inputs([0, 1, 0, 0])) == 4

def test_normalization_2qubit_3len():
    assert len(q_c.normalize_inputs([1.2, 1.5, 1j, 0])) == 4