#!/usr/bin/env python3
import serial
import sys

if(len(sys.argv) > 1 and sys.argv[1] == "1"):
	dev = serial.Serial("/dev/ttyACM1", 115200)
else:
	dev = serial.Serial("/dev/ttyACM0", 115200)

print("> Returned data:", file=sys.stderr)

while True:
    x = dev.read()
    sys.stdout.buffer.write(x)
    sys.stdout.flush()
