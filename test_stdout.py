import sys

# Standard output - sys.stdout

x = 125
y = "Masha"
print("Hello", str(x), y, "from print function")
sys.stdout.write(f'Hello {x} and {y}\n')
