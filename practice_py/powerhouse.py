import time
import sys

def type_print(text, delay=0.05):
    """Prints text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to next line after finishing


lyrics = """
Coo coo coolie power house-eh
Ennaikum koraiyatha movusu-eh
Un mela elasungalukkum
Perusugalukkum podusungalukkum
Paamaranukkum kumarigalukkum
Loves-eh 
Love you love you love you love
Love love love
"""

# Print each line slowly
for line in lyrics.split("\n"):
    type_print(line, delay=0.1)  # Adjust delay for speed
