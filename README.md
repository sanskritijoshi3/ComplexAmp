# ComplexAmp
Code for QOSF Mentorship cohort 11 screening task

Used Resources: 
https://pennylane.ai/blog/2025/10/state-preparation
https://quantum.cloud.ibm.com/learning/en/courses/quantum-machine-learning/data-encoding#encoding-at-arbitrary-points

Task 2: Complex Amplitudes

Goal: Given a input of complex ampltiudes [a00, a01, a10, a11] corresponding to $\psi = a00|00> + a01|01> + a10|10> + a11|11>$, normalize and implement the routine that would prepare this 2-qubit state.

Input: Complex ampltiudes [a00, a01, a10, a11]
Output: Routine to prepare this state

Theory:

Step 1: Normalize inputs

For any wavefunction $\psi = a00|00> + a01|01> + a10|10> + a11|11>$, |a00|^2 + |a01|^2 + |a10|^2 + |a11|^2 = 1. If that is not true, then all the ampltudes are divided by $\sqrt(|a00|^2 + |a01|^2 + |a10|^2 + |a11|^2)$ to normalize the inputs.

Step 2: Create the routine to set the magnitudes

Focusing on the real part, using Ry gates for 2-qubits, we can use an Ry gate, and anti-control 


