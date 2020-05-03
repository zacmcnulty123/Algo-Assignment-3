import argparse
import sys

def makeInput(arg):
  r=open("input/generatedInput/isInterleaved.txt", "w+")
  basicX = "101"
  basicY = "0"
  basicS = basicX + basicY + basicX + basicY
  result = basicS
  for i in range(0, int(arg)):
    result = result + basicS
  r.write(basicX + " " + basicY + " " + result)
  r.close()
  print("Look in input/generatedInput/ for the file")

parser = argparse.ArgumentParser()
parser.add_argument("-il", help="Makes very simple interleaved input for complexity trace runs. Creates a combo of 101 and 0 repeated input length times", type=makeInput, action="store")

if len(sys.argv) <= 1:
  sys.argv.append('--help')

options = parser.parse_args()
