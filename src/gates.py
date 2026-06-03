"""Gate parameters for simple CMOS logical effort calculations."""

# Each entry stores:
# g = logical effort, which compares the input capacitance of a gate to an inverter
# p = parasitic delay, which models internal diffusion capacitance effects
GATES = {
    "INV": {"g": 1.0, "p": 1.0},
    "NAND2": {"g": 4.0 / 3.0, "p": 2.0},
    "NOR2": {"g": 5.0 / 3.0, "p": 2.0},
}


def get_gate_names():
    """Return the available CMOS gate names."""
    return list(GATES.keys())


def get_gate_parameters(gate_name):
    """Return logical effort parameters for one gate.

    Parameters
    ----------
    gate_name : str
        Name of the gate, such as "INV", "NAND2", or "NOR2".
    """
    return GATES[gate_name]
