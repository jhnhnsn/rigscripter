# rigscripter

Manuals:
http://www.hfelectronics.nl/docs/Manuals/FT-991A_Manual.pdf
https://www.yaesu.com/downloadFile.cfm?FileID=13370&FileCatID=158&FileName=FT%2D991A%5FCAT%5FOM%5FENG%5F1711%2DD.pdf&FileContentType=application%2Fpdf

Module for scripting Yaesu FT991a. Making a module with functions to call CAT commands on my radio. Here's what I have so far:

#Swap VFOs
atob() --> Swaps VFOA to VFOB
btoa() --> Swaps VFOB to VFOA

#Antenna tuner control for current VFO (A or B):
get_at() --> Returns True if antenna tuner is on, False if it's off
set_at(state) --> Pass state = True to turn antenna tuner on, False to turn it off
atstart() --> Starts tuning

#AF Gain
get_afgain() --> Returns an int of the current gain
set_afgain(gain) --> Set AF gain with an int between 0 - 254

#Tune VFO in Hz
get_vfo(vfo, format="hz") --> Returns frequency for a VFO (VFO_A or VFO_B). Options: "hz", "string", or "raw"
set_vfo(vfo, freq_hz) --> Set a VFO to a frequency given in Hz

#Menu items
#CAT rate
get_catrate() --> returns an int of current CAT baud rate