# rigscripter

Module for scripting Yaesu FT991a. Making a module with functions to call CAT commands on my radio. Here's what I have so far:

VFO swaps:
atob() --> Swaps VFOA to VFOB
btoa() --> Swaps VFOB to VFOA

Antenna tuner control:
atstate() --> Returns True if antenna tuner is on, False if it's off
atcontrol(state) --> Pass state = "on" to turn antenna tuner on, "off" to turn it off
atstart() --> Starts tuning