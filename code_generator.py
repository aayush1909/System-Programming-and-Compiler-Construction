with open('input') as f:
   lines = f.readlines()
lines = [x.strip() for x in lines]
output, registers = [], []
start_register = 0  # ASCII for '1'
register_no = [1, 2, 3, 4, 5]

for n1, i in enumerate(lines):
   LHS, RHS = '', ''
   register_no = [0, 1, 2, 3, 4, 5]
   for n2, j in enumerate(i):

      if 'A' <= j <= 'Z':
         if j in [x[1] for x in registers]:
            registers.append(registers.pop([x[1] for x in registers].index(j)))
         else:                                                                           # not for LHS variables
            registers.append(['R' + str(register_no[0]), j])
            output.append('MOV ' + 'R' + str(register_no[0]) + ' ' + j)
            register_no.pop(0)

      if j == '=':                        # Undo
         popped = output.pop(-1)
         LHS = popped[-1]
         register_no.append(registers[0][-1])
         registers.pop(-1)

   if '+' in i:
      output.append('ADD ' + registers[-1][0] + ' ' + registers[-2][0])
      registers[-1][1] = LHS
   elif '-' in i:
      output.append('SUB ' + registers[-1][0] + ' ' + registers[-2][0])
      registers[-1][1] = LHS
   elif '*' in i:
      output.append('MUL ' + registers[-1][0] + ' ' + registers[-2][0])
      registers[-1][1] = LHS
   elif '/' in i:
      output.append('DIV ' + registers[-1][0] + ' ' + registers[-2][0])
      registers[-1][1] = LHS

   # if LHS != '':
   #  output.append('MOV ' + LHS + ' ' + registers[-1][0] )
   #  start_register += 1

   print(registers)
[print(_) for _ in output]

