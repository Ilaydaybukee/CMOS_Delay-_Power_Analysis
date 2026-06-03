"""Simple normalized delay model using logical effort."""


def logical_effort_delay(g, fanout, p):
    """Calculate normalized delay.

    The logical effort delay model is:

        d = g * fanout + p

    where:
    g      = logical effort of the gate
    fanout = load capacitance divided by input capacitance
    p      = parasitic delay of the gate

    The result is normalized, so it has no seconds unit. It is useful for
    comparing gates and loads before doing a detailed transistor-level design.
    """
    return g * fanout + p
