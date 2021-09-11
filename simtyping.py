import time
import sys
import argparse
from pynput.keyboard import Key, Controller

person_delimiter = "=="

parser = argparse.ArgumentParser(description='Read two input files that make up  a text conversation and send to open Windows')
parser.add_argument('-i', '--input', dest='infile', type=argparse.FileType('r'), \
    required=True, metavar='INPUT_FILE', help='The input file')
parser.add_argument('-p1', '--person1', dest='person1',required=True, metavar='PERSON1', help='Person 1 in the conversation')
parser.add_argument('-p2', '--person2', dest='person2',required=True, metavar='PERSON2', help='Person 2 in the conversation')
parser.add_argument('-ts1', '--typing-speed', dest='ts1', type=float, default=0.12)
parser.add_argument('-c', '--countdown', type=int, dest='countdown', default=5)




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
        time.sleep(millseconds)



contents = args.infile.readlines()

args.infile.close()

for line in contents:
    if person_delimiter in line:
            current_person = line.split(person_delimiter)
            #print(args.person1 + ' is about to speak')
            countdown(current_person[0], args.countdown)
            current_sentence = (current_person[1])
            sendthekeys(current_sentence,args.ts1) 


print('Conversation has ended')







