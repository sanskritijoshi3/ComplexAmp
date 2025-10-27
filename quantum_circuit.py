# quantum_circuit.py

#import libraries
import numpy as np
import cmath, math
from qiskit import QuantumCircuit

def normalize_inputs(list):
    sum = 0
    #calculate the sum of the amplitudes squared
    for elem in list:
        sum += pow(abs(elem),2)

    if sum == 1:
        return list
    else: #normalize the input if not already normalized.
        for i in range(len(list)):
            list[i] = list[i]/cmath.sqrt(sum)
        return list
    
#use Ry gates to implement creation of the real parts of the amplitudes
def create_Ry_gates(list):
    thetal = 2*math.acos(math.sqrt(pow(abs(list[0]), 2)+pow(abs(list[1]), 2)))
    theta_0 = 2*math.acos(math.sqrt(pow(abs(list[0]),2)/(pow(abs(list[0]), 2)+pow(abs(list[1]), 2))))
    theta_1 = 2*math.acos(math.sqrt(pow(abs(list[2]),2)/pow(abs(list[2]),2)))
    theta = [thetal, theta_0, theta_1]
    return theta

#use the Rz/phase gates to implement the complex phases of the complex amplitudes
def create_phase(list):
    phi00 = 0 #global phase
    phi01 = np.angle(list[1])- np.angle(list[0]) #phase of second qubit controlled by the first qubit
    phi10 = np.angle(list[2])- np.angle(list[0]) #phase of the first qubit relative to its phase phi00
    phi11 = np.angle(list[3])- np.angle(list[2]) - np.angle(list[1]) + np.angle(list[0])
    phases = [phi00, phi01, phi10, phi11]
    return phases

def create_circuit(theta, phases):
    qc = QuantumCircuit(2, name="Complex Ampltiude")

    # Step 2: Amplitude Encoding
    qc.ry(theta[0], 0)
    # X , CRy , X pattern to emulate an anti-control gate
    qc.x(0)
    qc.cry(theta[1], 0, 1)
    qc.x(0)
    qc.cry(theta[2], 0, 1)

    # Step 3: Phase Encoding
    qc.rz(phases[2], 0)
    # X , CRz , X pattern to emulate an anti-control gate
    qc.x(0)
    qc.crz(phases[1], 0, 1)
    qc.x(0)
    qc.crz(phases[3], 0, 1)

    return qc

if __name__ == "__main__":
    #prompt user for the amplitudes of their qubits
    user_input_str = input("Enter amplitudes separated by spaces: ")
    string_amplitudes = user_input_str.split() #turn input into a list
    amplitudes_list = [complex(s) for s in string_amplitudes]#create list into complex list

    #convert list into a numpy array
    amplitudes = np.array(amplitudes_list)
    #1. check the input is valid

    #check that the list has four elements
    if not len(amplitudes) == 4:
        raise TypeError("The list should have 4 elements")
    #check that every element is a complex number
    for elem in amplitudes:
        elem = complex(elem)
        if not isinstance(elem, complex):
            raise TypeError("Array elements are not complex numbers")
    #check that the inputs are normalized/normalize the inputs
    norm_input = normalize_inputs(amplitudes)
    print("normalized input: " + str(norm_input))
    theta = create_Ry_gates(norm_input)
    phase = create_phase(norm_input)
    qc = create_circuit(theta, phase)
    qc.draw("mpl", filename='complexamp.png')


