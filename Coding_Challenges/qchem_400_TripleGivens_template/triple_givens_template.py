import sys
import pennylane as qml
from pennylane import numpy as np

NUM_WIRES = 6


def triple_excitation_matrix(gamma):
    """The matrix representation of a triple-excitation Givens rotation.

    Args:
        - gamma (float): The angle of rotation

    Returns:
        - (np.ndarray): The matrix representation of a triple-excitation
    """

    # QHACK #
    c = qml.math.cos(gamma / 2)
    s = qml.math.sin(gamma / 2)

    mat = qml.math.diag([1.0] * 7 + [c] + [1.0] * 48 + [c] + [1.0] * 7)
    mat = qml.math.scatter_element_add(mat, (7, 56), -s)
    mat = qml.math.scatter_element_add(mat, (56, 7), s)

    return mat
    # QHACK #


dev = qml.device("default.qubit", wires=6)


@qml.qnode(dev)
def circuit(angles):
    """Prepares the quantum state in the problem statement and returns qml.probs

    Args:
        - angles (list(float)): The relevant angles in the problem statement in this order:
        [alpha, beta, gamma]

    Returns:
        - (np.tensor): The probability of each computational basis state
    """

    # QHACK #
    #first, prepare the state |111000>
    qml.BasisState(np.array([1, 1, 1, 0, 0, 0]), wires=[0, 1, 2, 3, 4, 5])

    qml.SingleExcitation(angles[0],wires=[0,5])
    qml.DoubleExcitation(angles[1], wires=[0,1,4,5])
    qml.QubitUnitary(triple_excitation_matrix(angles[2]), wires=[0,1,2,3,4,5])

    # QHACK #

    return qml.probs(wires=range(NUM_WIRES))


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = np.array(sys.stdin.read().split(","), dtype=float)
    probs = circuit(inputs).round(6)
    print(*probs, sep=",")
