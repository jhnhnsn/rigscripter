# rigscripter

Manuals:
http://www.hfelectronics.nl/docs/Manuals/FT-991A_Manual.pdf
https://www.yaesu.com/downloadFile.cfm?FileID=13370&FileCatID=158&FileName=FT%2D991A%5FCAT%5FOM%5FENG%5F1711%2DD.pdf&FileContentType=application%2Fpdf

Module for scripting Yaesu FT991a. Making a module with functions to call CAT commands on my radio. Here's what I have so far:

VFO swaps:
atob() --> Swaps VFOA to VFOB
btoa() --> Swaps VFOB to VFOA

Antenna tuner control:
atstate() --> Returns True if antenna tuner is on, False if it's off
atcontrol(state) --> Pass state = "on" to turn antenna tuner on, "off" to turn it off
atstart() --> Starts tuning