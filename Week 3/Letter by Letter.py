import sys
import time

def typewriter_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Forces the character to appear immediately
        time.sleep(delay)
    print()  # Prints a final newline at the end

# Example usage:
typewriter_print("Typing Letter by Letter...")