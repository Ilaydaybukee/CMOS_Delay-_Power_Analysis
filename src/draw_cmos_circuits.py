"""Draw simple educational static CMOS circuit diagrams.

The diagrams are schematic-style teaching drawings. They are not meant to
replace a professional EDA schematic, but they show the correct pull-up and
pull-down transistor connections for an inverter, NAND2, and NOR2 gate.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CIRCUITS_DIR = PROJECT_ROOT / "circuits"


def setup_axis(title):
    """Create a clean drawing area with no axes."""
    figure, axis = plt.subplots(figsize=(8, 7))
    axis.set_title(title, fontsize=16, pad=14)
    axis.set_xlim(0, 10)
    axis.set_ylim(0, 10)
    axis.set_aspect("equal")
    axis.axis("off")
    return figure, axis


def draw_wire(axis, x1, y1, x2, y2, linewidth=2):
    """Draw one straight wire segment."""
    axis.plot([x1, x2], [y1, y2], color="black", linewidth=linewidth)


def draw_node(axis, x, y):
    """Draw a filled connection dot."""
    axis.add_patch(Circle((x, y), 0.07, color="black"))


def draw_note(axis, x, y, text):
    """Draw explanatory text in open space."""
    axis.text(
        x,
        y,
        text,
        fontsize=11,
        va="center",
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 2},
    )


def draw_ground(axis, x, y):
    """Draw a simple ground symbol."""
    draw_wire(axis, x, y + 0.35, x, y)
    draw_wire(axis, x - 0.35, y, x + 0.35, y)
    draw_wire(axis, x - 0.22, y - 0.18, x + 0.22, y - 0.18)
    draw_wire(axis, x - 0.1, y - 0.36, x + 0.1, y - 0.36)
    axis.text(x + 0.45, y - 0.08, "GND", fontsize=12, va="center")


def draw_vdd(axis, x, y):
    """Draw a simple VDD supply rail label."""
    draw_wire(axis, x - 0.45, y, x + 0.45, y)
    axis.text(x + 0.6, y, "VDD", fontsize=12, va="center")


def draw_mos(
    axis,
    x,
    y,
    kind,
    name,
    input_label=None,
    label_dx=0.38,
    label_dy=0.0,
    input_dx=-1.55,
    input_dy=0.15,
):
    """Draw a simplified MOS transistor.

    The source and drain are shown as a vertical conduction path. The gate is
    the plate on the left. PMOS devices include a small gate bubble.
    """
    color = "#0b5cab" if kind == "PMOS" else "#126b2f"

    # Source/drain conduction path.
    draw_wire(axis, x, y + 0.55, x, y + 0.25)
    draw_wire(axis, x, y - 0.25, x, y - 0.55)
    draw_wire(axis, x - 0.18, y + 0.25, x + 0.18, y + 0.25, linewidth=2.4)
    draw_wire(axis, x - 0.18, y - 0.25, x + 0.18, y - 0.25, linewidth=2.4)

    # Gate plate and optional PMOS bubble.
    draw_wire(axis, x - 0.55, y - 0.38, x - 0.55, y + 0.38, linewidth=2.4)
    if kind == "PMOS":
        axis.add_patch(Circle((x - 0.38, y), 0.1, fill=False, linewidth=2))
        draw_wire(axis, x - 0.28, y, x - 0.1, y)

    axis.text(
        x + label_dx,
        y + label_dy,
        f"{name}\n{kind}",
        fontsize=10,
        va="center",
        color=color,
    )
    if input_label:
        axis.text(x + input_dx, y + input_dy, input_label, fontsize=12, ha="right")
        draw_wire(axis, x - 1.45, y, x - 0.55, y)


def save_figure(figure, filename):
    """Save one figure into the circuits folder."""
    CIRCUITS_DIR.mkdir(exist_ok=True)
    figure.savefig(CIRCUITS_DIR / filename, dpi=160, bbox_inches="tight")
    plt.close(figure)


def draw_cmos_inverter():
    """Draw a static CMOS inverter."""
    figure, axis = setup_axis("Static CMOS Inverter")

    draw_vdd(axis, 5, 8.8)
    draw_wire(axis, 5, 8.8, 5, 7.1)
    draw_mos(axis, 5, 6.5, "PMOS", "P1")
    draw_wire(axis, 5, 5.95, 5, 5.0)
    draw_node(axis, 5, 5.0)
    draw_wire(axis, 5, 5.0, 7.2, 5.0)
    axis.text(7.35, 5.0, "OUT", fontsize=12, va="center")

    draw_wire(axis, 5, 5.0, 5, 3.95)
    draw_mos(axis, 5, 3.4, "NMOS", "N1")
    draw_wire(axis, 5, 2.85, 5, 2.0)
    draw_ground(axis, 5, 1.55)

    axis.text(1.1, 5.0, "IN", fontsize=12, va="center")
    draw_wire(axis, 1.6, 5.0, 2.2, 5.0)
    draw_wire(axis, 2.2, 6.5, 3.55, 6.5)
    draw_wire(axis, 2.2, 3.4, 3.55, 3.4)
    draw_wire(axis, 2.2, 3.4, 2.2, 6.5)
    draw_node(axis, 2.2, 5.0)
    draw_wire(axis, 3.55, 6.5, 4.45, 6.5)
    draw_wire(axis, 3.55, 3.4, 4.45, 3.4)

    save_figure(figure, "cmos_inverter.png")


def draw_cmos_nand2():
    """Draw a static CMOS 2-input NAND gate."""
    figure, axis = setup_axis("Static CMOS NAND2")

    draw_vdd(axis, 5, 8.9)
    draw_wire(axis, 5, 8.9, 5, 8.25)
    draw_wire(axis, 3.8, 8.25, 6.2, 8.25)

    # PMOS pull-up network: two PMOS devices in parallel.
    draw_wire(axis, 3.8, 8.25, 3.8, 7.35)
    draw_mos(axis, 3.8, 6.8, "PMOS", "P1", "A", label_dx=0.45, label_dy=-0.72)
    draw_wire(axis, 3.8, 6.25, 3.8, 5.75)
    draw_wire(axis, 6.2, 8.25, 6.2, 7.35)
    draw_mos(axis, 6.2, 6.8, "PMOS", "P2", "B", input_dx=-1.15)
    draw_wire(axis, 6.2, 6.25, 6.2, 5.75)
    draw_wire(axis, 3.8, 5.75, 6.2, 5.75)

    # Output node between pull-up and pull-down networks.
    draw_wire(axis, 5, 5.75, 5, 5.25)
    draw_node(axis, 5, 5.25)
    draw_wire(axis, 5, 5.25, 7.4, 5.25)
    axis.text(7.55, 5.25, "OUT = NOT(A.B)", fontsize=12, va="center")

    # NMOS pull-down network: two NMOS devices in series.
    draw_wire(axis, 5, 5.25, 5, 4.45)
    draw_mos(axis, 5, 3.9, "NMOS", "N1", "A")
    draw_wire(axis, 5, 3.35, 5, 2.95)
    draw_node(axis, 5, 2.95)
    draw_mos(axis, 5, 2.4, "NMOS", "N2", "B")
    draw_wire(axis, 5, 1.85, 5, 1.5)
    draw_ground(axis, 5, 1.15)

    draw_note(axis, 0.75, 9.25, "Pull-up: PMOS in parallel")
    draw_note(axis, 0.75, 0.55, "Pull-down: NMOS in series")

    save_figure(figure, "cmos_nand2.png")


def draw_cmos_nor2():
    """Draw a static CMOS 2-input NOR gate."""
    figure, axis = setup_axis("Static CMOS NOR2")

    draw_vdd(axis, 5, 8.9)
    draw_wire(axis, 5, 8.9, 5, 8.2)

    # PMOS pull-up network: two PMOS devices in series.
    draw_mos(axis, 5, 7.6, "PMOS", "P1", "A")
    draw_wire(axis, 5, 7.05, 5, 6.35)
    draw_node(axis, 5, 6.35)
    draw_mos(axis, 5, 5.8, "PMOS", "P2", "B")
    draw_wire(axis, 5, 5.25, 5, 4.95)

    # Output node between pull-up and pull-down networks.
    draw_node(axis, 5, 4.95)
    draw_wire(axis, 5, 4.95, 7.4, 4.95)
    axis.text(7.55, 4.95, "OUT = NOT(A+B)", fontsize=12, va="center")

    # NMOS pull-down network: two NMOS devices in parallel.
    draw_wire(axis, 5, 4.95, 5, 4.55)
    draw_wire(axis, 3.8, 4.55, 6.2, 4.55)
    draw_wire(axis, 3.8, 4.55, 3.8, 3.65)
    draw_mos(axis, 3.8, 3.1, "NMOS", "N1", "A", label_dx=0.45, label_dy=-0.72)
    draw_wire(axis, 3.8, 2.55, 3.8, 2.0)
    draw_wire(axis, 6.2, 4.55, 6.2, 3.65)
    draw_mos(axis, 6.2, 3.1, "NMOS", "N2", "B", input_dx=-1.05)
    draw_wire(axis, 6.2, 2.55, 6.2, 2.0)
    draw_wire(axis, 3.8, 2.0, 6.2, 2.0)
    draw_wire(axis, 5, 2.0, 5, 1.5)
    draw_ground(axis, 5, 1.15)

    draw_note(axis, 0.75, 9.25, "Pull-up: PMOS in series")
    draw_note(axis, 0.75, 0.55, "Pull-down: NMOS in parallel")

    save_figure(figure, "cmos_nor2.png")


def main():
    """Create the circuits folder and save all circuit diagrams."""
    CIRCUITS_DIR.mkdir(exist_ok=True)
    draw_cmos_inverter()
    draw_cmos_nand2()
    draw_cmos_nor2()
    print(f"Circuit diagrams saved in: {CIRCUITS_DIR}")


if __name__ == "__main__":
    main()
