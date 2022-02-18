#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml


def qfunc_adder(m, wires):
    """Quantum function capable of adding m units to a basic state given as input.

    Args:
        - m (int): units to add.
        - wires (list(int)): list of wires in which the function will be executed on.
    """

    qml.QFT(wires=wires)

    # QHACK #



    #solution 1
    #performs a phase shift on each qubit according to the value
    #of the bits of the adding number (m), as explicitly shown in Draper
    # mm = format(m, f'0{len(wires)}b')
    # print(f'raw mm: {mm}')
    # mm = [int(x) for x in mm]
    #
    # def phi(l, bit):
    #     return 2 * np.pi * bit / 2.0**l
    #
    # mm.reverse()
    # for w in wires: #starting with 0...
    #     print(f'wire/qubit index: {w}')
    #     total_phi = 0
    #     for l in range(w+1):
    #         _phi = phi(l+1, mm[w - l])
    #         print(f'l {l}, phase_shift_l+1 {l+1} ( bit_{w-l} = {mm[w-l]} ): phi = {_phi}')
    #         qml.PhaseShift(_phi, wires=w)
    #         total_phi += _phi
    #     print(f'total phase shift phi: {total_phi}')

    #solution 2
    #combines each of the individual phase shifts above into a single phase shift
    #by computing the appropriate binary fraction

    mm = format(m, f'0{len(wires)}b')

    def binary_fraction(s):
        return int(s, 2) / 2.**(len(s))

    for w in wires: #starting with 0...
        #print(f'wire/qubit index: {w}')
        _phi = 2*np.pi*binary_fraction(mm[len(mm)- 1 - w:])
        #print(f'phase shift phi: {_phi}')
        qml.PhaseShift(_phi, wires=w)

    # QHACK #

    qml.QFT(wires=wires).inv()


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    m = int(inputs[0])
    n_wires = int(inputs[1])
    wires = range(n_wires)

    dev = qml.device("default.qubit", wires=wires, shots=1)

    @qml.qnode(dev)
    def test_circuit():
        # Input:  |2^{N-1}>
        qml.PauliX(wires=0)

        qfunc_adder(m, wires)
        return qml.sample()

    output = test_circuit()
    print(*output, sep=",")
