#!/usr/bin/python3
import multiprocessing

# Use 'multiprocessing.cpu_count()' to determine the number of available CPU cores.
cpu_count = multiprocessing.cpu_count()

print(cpu_count)    # Print the number of CPU cores available on the system.
