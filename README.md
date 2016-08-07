Light Sleeper
========
This is a python project using a Rapberry Pi 2 to drive an LED in a pulsing pattern.
The pulse rate changes between a starting value and end ending value in a linear ramp,
for a constant time period.  After reaching the lower value, it runs for another constant
amount of time at the slowest value.   

Currently, all values are hardcoded in the script.

The LED will start when you press button 1, and will through the 20 min cycle.
The LED will stop when you press button 2.

#### Usage instructions
Press Button 1 to start a cycle.
Press Button 2 to shut off LED.

#### Future enhancements
Add a different, selectable cycle length.
Add starting and stopping breathing rates, controllable via a text file setting.
Perhaps also have cycle lengths in text file, and allow it to be selectable.
