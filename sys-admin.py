import os
import subprocess

# OLD WAY (works but not recommended)
print("Running ls using os.system:")
os.system("ls")

print("\n----------------------\n")

# MODERN WAY (recommended)
print("Running ls using subprocess.run:")
subprocess.run(["ls"])

print("\nRunning ls -l:")
subprocess.run(["ls", "-l"])

print("\nRunning ls -l README.md:")
subprocess.run(["ls", "-l", "README.md"])

print("\n----------------------\n")

# uname -a
command = "uname"
commandArgument = "-a"
print(f"Gathering system information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])

print("\n----------------------\n")

# ps -x
command = "ps"
commandArgument = "-x"
print(f"Gathering active process information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])
