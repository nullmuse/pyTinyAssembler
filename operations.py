import time
import random
from sys import exit,stdout
import os
random.seed()
memory = []
code = []
tip = 0



def init_mem(num):
   global memory
   for item in range(num):
      memory.append(0)



class Op:
   def __init__(self,opcodes, func=None):
      self.func = func
      self.opcodes = opcodes
      self.fstr = '0x{:02x} '
   def assemble(self, ops):
      op_index = -1
      retops = []
      counter = 0
      ops = ops.split()[1:]
      for item in ops:
         if '[' in item:
            op_index +=1
            retops.append(list(item)[1])
            if counter >= 1 and op_index == 0:
               op_index += 1
         if '[' not in item:
            retops.append(item)
         counter += 1
      if counter == 1:
         op_index += 1
      if op_index != -1:
         self.opcodes.reverse()
         assembled_str = self.opcodes[op_index] + ' '
         self.opcodes.reverse()
      else:
         assembled_str = self.opcodes[op_index] + ' '
      for item in retops:
         assembled_str +=  self.fstr.format(int(item))
      return assembled_str








def op_and(statement, opcodes):
   global memory
   statement = statement.split() 
   opcodes.reverse() 
   op_type = opcodes.index(statement[0])
   if op_type:
      memory[int(statement[1][2:])] &=  memory[int(statement[2][2:])]
   else:
      memory[int(statement[1][2:])] &= int(statement[2][2:])
   

def op_or(statement, opcodes):
   global memory
   statement = statement.split()
   opcodes.reverse()   
   op_type = opcodes.index(statement[0])
   if op_type:   
       memory[int(statement[1][2:])] |=  memory[int(statement[2][2:])]
   else:
      memory[int(statement[1][2:])] &= int(statement[2][2:])

def op_xor(statement, opcodes):
   global memory
   statement = statement.split()
   opcodes.reverse()
   op_type = opcodes.index(statement[0])
   if op_type:
       memory[int(statement[1][2:])] ^=  memory[int(statement[2][2:])]
   else:
      memory[int(statement[1][2:])] ^= int(statement[2][2:])


def op_not(statement, opcodes):
   global memory
   statement = statement.split()
   memory[int(statement[1][2:])] =  ~memory[int(statement[1][2:])]

def op_mov(statement, opcodes):
   global memory
   statement = statement.split()
   opcodes.reverse()
   op_type = opcodes.index(statement[0])
   if op_type:
       memory[int(statement[1][2:])] =  memory[int(statement[2][2:])]
   else:
      memory[int(statement[1][2:])] = int(statement[2][2:])

def op_rand(statement, opcodes):
   global memory
   memory[int(statement[1][2:])] = random.choice(range(26))

def op_add(statement, opcodes):
   global memory
   statement = statement.split()
   opcodes.reverse()
   op_type = opcodes.index(statement[0])
   if op_type:
       memory[int(statement[1][2:])] +=  memory[int(statement[2][2:])]
   else:
      memory[int(statement[1][2:])] += int(statement[2][2:])


def op_sub(statement, opcodes):
   global memory
   statement = statement.split()
   opcodes.reverse()
   op_type = opcodes.index(statement[0])
   if op_type:
       memory[int(statement[1][2:])] -=  memory[int(statement[2][2:])]
   else:
      memory[int(statement[1][2:])] -= int(statement[2][2:])

def op_jmp(statement, opcodes):
   global memory
   global tip 
   statement = statement.split()
   op_type = opcodes.index(statement[0])
   if op_type:
      tip += memory[int(statement[1][2:])]
   else:
      tip += int(statement[1][2:])

def op_jz(statement, opcodes):
   global memory
   global tip 
   statement = statement.split()
   opcodes.reverse()
   op_type = opcodes.index(statement[0])
   if op_type == 0:
      if  int(statement[2][2:]) == 0:
         tip += int(statement[1][2:])
   elif op_type == 1:
      if memory[int(statement[2][2:])] == 0:
          print(tip)
          tip += int(statement[1][2:])
          print(tip)
   elif op_type == 2:
       if  int(statement[2][2:]) == 0:
          tip += memory[int(statement[1][2:])]
   elif op_type == 3:
       if  memory[int(statement[2][2:])] == 0:
          tip += memory[int(statement[1][2:])]

def op_jeq(statement, opcodes):
   global memory
   global tip
   statement = statement.split()
   opcodes.reverse()
   op_type = opcodes.index(statement[0])
   if op_type == 0:
      if  memory[int(statement[2][2:])] == int(statement[3][2:]):
         tip += int(statement[1][2:])
   elif op_type == 1:
      if memory[int(statement[2][2:])] == int(statement[3][2:]):
          tip += memory[int(statement[1][2:])]
   elif op_type == 2:
       if memory[int(statement[2][2:])] == memory[int(statement[3][2:])]:
          tip += int(statement[1][2:])
   elif op_type == 3:
       if memory[int(statement[2][2:])] == memory[int(statement[3][2:])]:
          tip += memory[int(statement[1][2:])]

def op_jls(statement, opcodes):
   global memory
   global tip
   statement = statement.split()
   opcodes.reverse()
   op_type = opcodes.index(statement[0])
   if op_type == 0:
      if  memory[int(statement[2][2:])] < int(statement[3][2:]):
         tip += int(statement[1][2:])
   elif op_type == 1:
      if memory[int(statement[2][2:])] < int(statement[3][2:]):
          tip += memory[int(statement[1][2:])]
   elif op_type == 2:
       if memory[int(statement[2][2:])] < memory[int(statement[3][2:])]:
          tip += int(statement[1][2:])
   elif op_type == 3:
       if memory[int(statement[2][2:])] < memory[int(statement[3][2:])]:
          tip += memory[int(statement[1][2:])]


def op_jgt(statement, opcodes):
   global memory
   global tip
   statement = statement.split()
   opcodes.reverse()
   op_type = opcodes.index(statement[0])
   if op_type == 0:
      if  memory[int(statement[2][2:])] > int(statement[3][2:]):
         tip += int(statement[1][2:])
   elif op_type == 1:
      if memory[int(statement[2][2:])] > int(statement[3][2:]):
          tip += memory[int(statement[1][2:])]
   elif op_type == 2:
       if memory[int(statement[2][2:])] > memory[int(statement[3][2:])]:
          tip += int(statement[1][2:])
   elif op_type == 3:
       if memory[int(statement[2][2:])] > memory[int(statement[3][2:])]:
          tip += memory[int(statement[1][2:])]


def op_halt(statement, opcodes):
   exit()

def op_aprint(statement, opcodes):
   global memory
   statement = statement.split()
   op_type = opcodes.index(statement[0])
   if op_type:
      val = str(int(statement[1][2:]))
      print(chr(int(val,16)), end='')
   else:
       val = str(memory[int(statement[1][2:])])
       print(chr(int(val,16)), end='')

def op_dprint(statement, opcodes):
   global memory
   statement = statement.split()
   op_type = opcodes.index(statement[0])
   if op_type:
       val = str(int(statement[1][2:]))
       print(int(val,16), end='')
   else:
       val = str(memory[int(statement[1][2:])])
       print(int(val,16), end='')



opcodes = {
"AND":Op(['0x00','0x01'], func=op_and),
"OR":Op(['0x02', '0x03'], func=op_or),
"XOR":Op(['0x04', '0x05'], func=op_xor),
"NOT":Op(['0x06'], func=op_not),
"MOV":Op(['0x07','0x08'], func=op_mov),
"RANDOM":Op(['0x09'], func=op_rand),
"ADD":Op(['0x0a', '0x0b'], func=op_add),
"SUB":Op(['0x0c', '0x0d'], func=op_sub),
"JMP":Op(['0x0e', '0x0f'], func=op_jmp),
"JZ":Op(['0x10', '0x11', '0x12', '0x13'], func=op_jz),
"JEQ":Op(['0x14', '0x15', '0x16', '0x17'], func=op_jeq),
"JLS":Op(['0x18', '0x19', '0x1a', '0x1b'], func=op_jls),
"JGT":Op(['0x1c', '0x1d', '0x1e', '0x1f'], func=op_jgt),
"HALT":Op(['0xff'], func=op_halt),
"APRINT":Op(['0x20', '0x21'], func=op_aprint),
"DPRINT":Op(['0x22', '0x23'], func=op_dprint)

}


def display_memory(memory):
   dat = 0
   for dword in range(len(memory) // 8):
      print('\t\t\t\t\t\t\t| 0x{0:02} | {1} '.format(int(hex(dat),16), ['0x{0:02}'.format(x) for x in memory[dat:dat + 8]]))
      dat += 8
   
def execute(asm):
   global code
   global tip
   global opcodes
   global memory
   init_mem(48)
   code = [x.strip() for x in asm]
   if code[-1] != '0xff':
      code.append('0xff')
   while True:
      print("\t\t\t\t\t\t\t| TIP | 0x{0:02}".format(int(hex(tip),16)))
      display_memory(memory)
      pip = int(tip)
      oper = code[tip].split()[0]
      for item in opcodes.items():
         if oper in item[1].opcodes:
            opcodes[item[0]].func(code[tip],list(item[1].opcodes))
      if pip == tip:
         tip += 1
      time.sleep(1)       
