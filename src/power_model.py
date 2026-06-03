"""Simple dynamic power model for CMOS gates."""


def dynamic_power(load_capacitance, vdd, frequency, switching_activity):
    """Calculate CMOS dynamic power.

    The dynamic power equation is:

        Pdyn = CL * VDD^2 * frequency * switching_activity

    where:
    CL                 = load capacitance in farads
    VDD                = supply voltage in volts
    frequency          = switching frequency in hertz
    switching_activity = probability that the output switches in one clock cycle

    The result is power in watts.
    """
    return load_capacitance * vdd**2 * frequency * switching_activity
