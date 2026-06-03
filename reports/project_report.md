# CMOS Logic Gates: Delay and Dynamic Power Analysis

## 1. Objective

The objective of this project is to analyze basic static CMOS logic gates using simple delay and dynamic power models. The project focuses on inverter, 2-input NAND, and 2-input NOR gates.

## 2. Theoretical Background

Static CMOS logic gates are built using complementary pull-up and pull-down networks. The pull-up network consists of PMOS transistors, while the pull-down network consists of NMOS transistors. In steady state, one of these networks connects the output either to VDD or to ground.

In this project, two main models are used:

### 2.1 Logical Effort Delay Model

The normalized delay is calculated as:

```text
d = g * fanout + p
```

where:

- d is the normalized delay,
- g is the logical effort,
- fanout is the effective output load,
- p is the parasitic delay.

The parameters used in this project are:

| Gate | g | p |
| --- | --- | --- |
| INV | 1 | 1 |
| NAND2 | 4/3 | 2 |
| NOR2 | 5/3 | 2 |

### 2.2 Dynamic Power Model

The dynamic power consumption is calculated as:

```text
Pdyn = CL * VDD^2 * frequency * switching_activity
```

where:

- CL is the load capacitance,
- VDD is the supply voltage,
- frequency is the switching frequency,
- switching_activity is the probability of output switching.

### 2.3 CMOS Gate Schematics

Static CMOS gates are implemented using complementary pull-up and pull-down networks. The pull-up network is built with PMOS transistors, while the pull-down network is built with NMOS transistors.

In the inverter, one PMOS and one NMOS transistor are used. In the NAND2 gate, the PMOS transistors are connected in parallel and the NMOS transistors are connected in series. In the NOR2 gate, the PMOS transistors are connected in series and the NMOS transistors are connected in parallel.

#### CMOS Inverter

![Static CMOS Inverter](../circuits/cmos_inverter.png)

#### CMOS NAND2

![Static CMOS NAND2](../circuits/cmos_nand2.png)

#### CMOS NOR2

![Static CMOS NOR2](../circuits/cmos_nor2.png)

## 3. Methodology

A Python project was created to calculate normalized delay and dynamic power. The project contains separate modules for gate parameters, delay calculation, power calculation, and plot generation.

The generated plots are:

- fanout_vs_delay.png
- vdd_vs_power.png
- frequency_vs_power.png
- capacitance_vs_power.png

## 4. Results and Discussion

### 4.1 Fanout vs Delay

![Fanout vs Normalized Delay](../plots/fanout_vs_delay.png)

The fanout-delay graph shows that delay increases as fanout increases. The inverter has the lowest delay because it has the smallest logical effort and parasitic delay. NAND2 has a higher delay than the inverter, and NOR2 has the highest delay among the three gates.

### 4.2 VDD vs Dynamic Power

![VDD vs Dynamic Power](../plots/vdd_vs_power.png)

The VDD-power graph shows that dynamic power increases nonlinearly with supply voltage. This is expected because dynamic power is proportional to VDD squared.

### 4.3 Frequency vs Dynamic Power

![Frequency vs Dynamic Power](../plots/frequency_vs_power.png)

The frequency-power graph shows a linear increase. As the switching frequency increases, the output capacitance is charged and discharged more often, increasing dynamic power consumption.

### 4.4 Load Capacitance vs Dynamic Power

![Load Capacitance vs Dynamic Power](../plots/capacitance_vs_power.png)

The capacitance-power graph also shows a linear increase. A larger load capacitance requires more energy during switching, so the dynamic power increases.

## 5. Conclusion

This project shows how fanout affects delay and how supply voltage, frequency, and load capacitance affect CMOS dynamic power consumption. The results agree with the theoretical behavior of static CMOS gates. The project provides a simple learning tool for understanding basic digital integrated circuit design concepts.