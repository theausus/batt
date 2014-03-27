Batt is an extremely lightweight battery monitor to be used from the terminal.
It is built to work on Linux but it should also work on OSX and (theoretically)
on Windows. Batt will detect all batteries and combine them to output the 
current total mWh, the total mWh when full, and the current charge percentage.

It uses the ACPI battery information and thus, will not work on systems not
using ACPI. If your system does not use /sys/class/power_supply to store its
power information, you can easily configure batt to use the proper directory
for your system. To do this, create a file in your home directory named
".battrc" contaning the full path to the directory (not including the final /).

NOTE: Batt uses Python 3.3 so it must be called using python3 until I make an installer.
