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
      if op_index != -1:
         self.opcodes.reverse()
         assembled_str = self.opcodes[op_index] + ' '
         self.opcodes.reverse()
      else:
         assembled_str = self.opcodes[op_index] + ' '
      for item in retops:
         assembled_str +=  self.fstr.format(int(item))
      return assembled_str

stack = []

opcodes = {
"AND":Op(['0x00','0x01']),
"OR":Op(['0x02', '0x03']),
"XOR":Op(['0x04', '0x05']),
"NOT":Op(['0x06']),
"MOV":Op(['0x07','0x08']),
"RANDOM":Op(['0x09']),
"ADD":Op(['0x0a', '0x0b']),
"SUB":Op(['0x0c', '0x0d']),
"JMP":Op(['0x0e', '0x0f']),
"JZ":Op(['0x10', '0x11', '0x12', '0x13']),
"JEQ":Op(['0x14', '0x15', '0x16', '0x17']),
"JLS":Op(['0x18', '0x19', '0x1a', '0x1b']),
"JGT":Op(['0x1c', '0x1d', '0x1e', '0x1f']),
"HALT":Op(['0xff']),
"APRINT":Op(['0x20', '0x21']),
"DPRINT":Op(['0x22', '0x23'])

}





def convert_source(filename):
   global opcodes
   source = open(filename).readlines()
   print("Original Source\n")
   for item in source:
      print(item.strip())
   assembly = [] 
   for item in source:
      item = item.strip()
      op_code = item.split()[0]
      assembly.append(opcodes[op_code.upper()].assemble(item))
      
   return assembly 





if __name__ == '__main__':
   from sys import argv
   
   asm = convert_source(argv[1])
   print("---------------------")
   print("Compiled TinyAssembly Machine Code:")
   for item in asm:
      print(item)







