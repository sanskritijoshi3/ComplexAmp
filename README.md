# ComplexAmp
Code for QOSF Mentorship cohort 11 screening task

Used Resources: 
https://pennylane.ai/blog/2025/10/state-preparation
https://quantum.cloud.ibm.com/learning/en/courses/quantum-machine-learning/data-encoding#encoding-at-arbitrary-points
https://arxiv.org/pdf/1003.5760
https://arxiv.org/pdf/2211.13039

Task 2: Complex Amplitudes

Goal: Given a input of complex ampltiudes [a00, a01, a10, a11] corresponding to $\psi = a00|00> + a01|01> + a10|10> + a11|11>$, normalize and implement the routine that would prepare this 2-qubit state.

Input: Complex ampltiudes [a00, a01, a10, a11]
Output: Routine to prepare this state

Theory:

Step 1: Normalize inputs

For any wavefunction $\psi = a00|00> + a01|01> + a10|10> + a11|11>$, |a00|^2 + |a01|^2 + |a10|^2 + |a11|^2 = 1. If that is not true, then all the ampltudes are divided by $\sqrt(|a00|^2 + |a01|^2 + |a10|^2 + |a11|^2)$ to normalize the inputs.

Step 2: Create the routine to set the magnitudes

Focusing on the real part, using Ry gates for 2-qubits, we can use an Ry gate, and anti-control and control Ry gates.

The control Ry gate (CRy) is represented by: $I \otimes ∣0⟩⟨0∣+RY \otimes ∣1⟩⟨1∣$
The anti-control Ry gate (ACRy) is represented by: $Ry \otimes ∣0⟩⟨0∣+ I \otimes ∣1⟩⟨1∣$

Using Fig. 1 from the Pennylane blog, we know that at |$\psi_0$> = |00>.

At $|\psi_1> = Ry|0> \otimes |0> = cos(\theta/2)|00> + 0|01> + sin(\theta/2)|10> + 0|11>.

At $|\psi_2> = ACRy |\psi_1> = $

At $|\psi_3> = CRy |\psi_2> = $

Therefore, we can calculate $\theta = 2arccos\sqrt{|a00|^{2} + |a01|^{2}}$, $\theta_0 = \sqrt{\frac{|a00|^{2}}{|a00|^{2} + |a01|^{2}}}$, $\theta_1 = \sqrt{\frac{|a10|^{2}}{|a10|^{2} + |a11|^{2}}}$.

Step 3: Create the routine to set the phases

We want an ampltiude that looks like: $|\psi> = ∣a00​∣e^{i\gamma_{00}}∣00⟩+∣a01​∣e^{i\gamma_{01}​}∣01⟩+∣a10​∣e^{i\gamma_{10}}∣10⟩+∣a11​∣e^{i\gamma_{11}}​∣11⟩$.

So we need to calculate the relative phases of each amplitude.

We can say that the phase $\gamma_{00}$ is the relative phase of the circuit, therefore we would take each of the phases and subtract $\gamma_{00}$ to remove any relative phase.

For the gates then, we need to apply 3 different gates for each ampltitude's phase:

$\phi_{01} = \gamma_01 - \gamma_00$

$\phi_{10} = \gamma_10 - \gamma_00$

$\phi_{11} = \gamma_11 - \gamma_01 - \gamma_10 + \gamma_00$

$\phi_{10}$ is applied on the first qubit with a Rz gate so it will apply when qubit 1 = 1

$\phi_{01} is applied on the second quibt with an anti-control Rz gate because we want it to apply when qubit 1 = 0 and qubit 2 = 1.

$\phi_{11} is applied on the second qubit with a control Rz gate because we want it to apply when qubit 1 = 1 and qubit 2 = 1.




