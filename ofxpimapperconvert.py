#!/usr/bin/python

import sys, getopt
from ffmpy import FFmpeg

def convert(input, output):
      ff = FFmpeg(
        inputs={input: None},
        outputs={output: '-c:v libx264 -preset medium -an '})
      ff.run()

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
      if not opts:
        sys.exit(2)
   except getopt.GetoptError:
      print("ofxpimapperconvert.py -i <inputfile> -o <outputfile>")
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
        inputfile = arg
      elif opt in ("-o", "--ofile"):
        outputfile = arg
   print (inputfile, outputfile)
   convert(inputfile, outputfile)


if __name__ == "__main__":
       main(sys.argv[1:])
