import os
import time

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Car shape using ASCII
car_shape = [
    "    ______",
    " __/[] [] \\__",
    "|_          _|",
    "  O--------O"
]

# Initial horizontal position
x_pos = 0

# Animation loop
while x_pos < 50:  # move car 50 steps
    clear_screen()  # clear previous frame

    # Print car at current position
    for line in car_shape:
        print(" " * x_pos + line)

    # Translate car to the right
    x_pos += 1

    # Control speed of animation
    time.sleep(0.05)
