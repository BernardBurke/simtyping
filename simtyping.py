import time
import sys
import argparse
from pynput.keyboard import Key, Controller

parser = argparse.ArgumentParser(description='Read two input files that make up  a text conversation and send to open Windows')
parser.add_argument('-i', '--input', dest='infile', type=argparse.FileType('r'), \
    required=True, metavar='INPUT_FILE', help='The input file')
parser.add_argument('-p1', '--person1', dest='person1',required=True, metavar='PERSON1', help='Person 1 in the conversation')
parser.add_argument('-p2', '--person2', dest='person2',required=True, metavar='PERSON2', help='Person 2 in the conversation')


args = parser.parse_args()
keyboard = Controller()

def countdown(speaker, seconds):
    sys.stdout.write(speaker + ' is about to speak')
    for remains in range(seconds,0,-1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remains))
        sys.stdout.flush
        time.sleep(1)

    sys.stdout.write("\rSpeaking")
        

def sendthekeys(words, millseconds):
    for char in words:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)



contents = args.infile.readlines()

args.infile.close()

for line in contents:
    if args.person1 in line:
            #print(args.person1 + ' is about to speak')
            countdown(args.person1, 10)
            print (line)
            sendthekeys(line,10) 
            








