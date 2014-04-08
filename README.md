#About

Batt is an extremely lightweight battery monitor to be used from the terminal.
It is built to work on Linux but it should also work on OSX and (theoretically)
on Windows. Batt will detect all batteries and combine them to output the 
current total mWh, the total mWh when full, and the current charge percentage.

It uses the ACPI battery information and thus, will not work on systems not
using ACPI. If your system does not use ```/sys/class/power_supply``` to store its
power information, you can easily configure batt to use the proper directory
for your system. To do this, create a file in your home directory named
".battrc" containing the full path to the directory (including the final /).

Example .battrc:
```
/proc/acpi/battery/
```

#Use Cases
* You use terminal extensively and you want to easily check your battery life.
* Your laptop contains multiple batteries and you want to quickly see the combined 
  charge percentage.
* Your desktop environment does not have a built in battery monitor (or it is
  disabled) and you want a simple way to check battery status.
* You want to quickly know the total current and full mWh for your batteries.

#Installation

Run
```
# python3 setup.py install
```

#Usage

From the terminal, type
```
$ batt
```
