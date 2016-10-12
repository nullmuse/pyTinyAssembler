#!/usr/bin/env python3.4

from operations import *
 

def convert_source(filename):
   global opcodes
   source = open(filename).readlines()
   print("Original Source\n")
   for item in source:
      print(item.strip())
   assembly = [] 
   for item in source:
      item = item.strip()
      print(item)
      op_code = item.split()[0]
      assembly.append(opcodes[op_code.upper()].assemble(item))
      
   return assembly 


def asm_writeout(assembly):
    print("Compiled TinyAssembly Machine Code:")
    for item in asm:
       print(item)





if __name__ == '__main__':
   from sys import argv
   asm = convert_source(argv[1])
   asm_writeout(asm)
   execute(asm)
