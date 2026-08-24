# V Y SURYA | 2026A7PS0144H | Avionics
TASKS FOR SEDS CLUB INDUCTION BPHC (THE AVIONICS TEAM) 
## TASK 1
* Completed without major issues by following the provided documentation and team resources.

* Graph Rendering Issue: The plot line colors were resetting/changing frame-by-frame during updates. Fixed this by explicitly initializing line and axis properties using matplotlib subplots beforehand.

* Data Noise & Smoothing: Implemented a basic moving average filter to handle noisy data. The script checks for unrealistic spikes/jumps and smooths them out by taking the mean of the previous two data points.

* Window Selection: Tested multiple window lengths, settling on two points to maintain local depth accuracy while filtering out sharp outliers within a tight context window.
## TASK 2
Task Overview

* Designed and assembled the Arduino schematic and component wiring to create a fully functional system.

Challenges & Fixes

* Circuit Organization: Initially ran into a mess of direct wiring; resolved this by introducing a breadboard to cleanly divide and route the circuit paths.

Component Protection:
* Overlooked the necessary pull-down/current-limiting resistors for sensitive components (LED and light sensor), which were added to stabilize signals and protect the hardware.

Software & Logic

* Adapted quickly to the C/C++ Arduino syntax by translating core logic concepts from Python.
