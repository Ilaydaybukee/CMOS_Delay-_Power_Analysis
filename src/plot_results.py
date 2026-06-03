"""Generate delay and dynamic power plots for basic static CMOS gates."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from delay_model import logical_effort_delay
from gates import GATES
from power_model import dynamic_power


# The plots folder is one level above this src folder.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
PLOTS_DIR = PROJECT_ROOT / "plots"


def plot_fanout_vs_delay():
    """Plot normalized delay versus fanout for INV, NAND2, and NOR2."""
    fanouts = np.arange(1, 11)

    plt.figure()
    for gate_name, parameters in GATES.items():
        delays = logical_effort_delay(
            parameters["g"],
            fanouts,
            parameters["p"],
        )
        plt.plot(fanouts, delays, marker="o", label=gate_name)

    plt.title("Fanout vs Normalized Delay")
    plt.xlabel("Fanout")
    plt.ylabel("Normalized delay, d = g * fanout + p")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "fanout_vs_delay.png", dpi=150)
    plt.close()


def plot_vdd_vs_power():
    """Plot dynamic power while changing supply voltage VDD."""
    vdd_values = np.linspace(0.8, 1.8, 11)
    load_capacitance = 10e-15
    frequency = 100e6
    switching_activity = 0.5

    power_values = dynamic_power(
        load_capacitance,
        vdd_values,
        frequency,
        switching_activity,
    )

    plt.figure()
    plt.plot(vdd_values, power_values * 1e6, marker="o")
    plt.title("VDD vs Dynamic Power")
    plt.xlabel("Supply voltage VDD (V)")
    plt.ylabel("Dynamic power (microW)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "vdd_vs_power.png", dpi=150)
    plt.close()


def plot_frequency_vs_power():
    """Plot dynamic power while changing switching frequency."""
    frequencies = np.linspace(10e6, 500e6, 11)
    load_capacitance = 10e-15
    vdd = 1.2
    switching_activity = 0.5

    power_values = dynamic_power(
        load_capacitance,
        vdd,
        frequencies,
        switching_activity,
    )

    plt.figure()
    plt.plot(frequencies / 1e6, power_values * 1e6, marker="o")
    plt.title("Frequency vs Dynamic Power")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Dynamic power (microW)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "frequency_vs_power.png", dpi=150)
    plt.close()


def plot_capacitance_vs_power():
    """Plot dynamic power while changing load capacitance CL."""
    capacitances = np.linspace(1e-15, 50e-15, 11)
    vdd = 1.2
    frequency = 100e6
    switching_activity = 0.5

    power_values = dynamic_power(
        capacitances,
        vdd,
        frequency,
        switching_activity,
    )

    plt.figure()
    plt.plot(capacitances * 1e15, power_values * 1e6, marker="o")
    plt.title("Load Capacitance vs Dynamic Power")
    plt.xlabel("Load capacitance CL (fF)")
    plt.ylabel("Dynamic power (microW)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "capacitance_vs_power.png", dpi=150)
    plt.close()


def main():
    """Create all plots and save them in the plots folder."""
    PLOTS_DIR.mkdir(exist_ok=True)
    plot_fanout_vs_delay()
    plot_vdd_vs_power()
    plot_frequency_vs_power()
    plot_capacitance_vs_power()
    print(f"Plots saved in: {PLOTS_DIR}")


if __name__ == "__main__":
    main()
