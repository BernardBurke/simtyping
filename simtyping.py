import time
import argparse
from pynput.keyboard import Key, Controller

parser = argparse.ArgumentParser(description='Read two input files that make up  a text conversation and send to open Windows')
parser.add_argument('-i', '--input', dest='infile', type=file, required=True, metavar='INPUT_FILE', help='The input file')

args = parser.parse_args()

infile=args.infile


keyboard = Controller()

time.sleep(50)

for char in "Good morning Bob. What's going on for you?":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)

