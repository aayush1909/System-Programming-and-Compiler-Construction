with open('grammar.txt') as f:
    grammar = f.readlines()
with open('table.txt') as f:
    table = f.readlines()

grammar= [a[3:] for a in grammar]
table = [a.strip() for a in table]
order = ['^', '*', '/', '+', '-', '(', ')', 'a', '$']
print(table)

input_buffer = input('Enter a string') + '$'
n = 0
stack = ['$']
pruning = ''

print(input_buffer , stack)

while n in range(len(input_buffer)) :
     operator = table[order.index(stack[-1])][order.index(input_buffer[n])]
     print('\n\n', '\nStack : ', stack, '\nCurrent input buffer element : ', input_buffer[n], '\nSign : ', operator)

     if operator == 'A':
         print('Accepted')
         exit(0)
     elif operator == 'E':
         print('Error')
         exit(0)

     elif operator == '<' :
         stack.append('<')
         if pruning != '' :
             stack.append(pruning)
             pruning = ''
         stack.append(input_buffer[n])

     elif operator == '>' :
         while stack[-1]!='<' :
             pruning += stack.pop(-1)
         stack.pop(-1)
         n -= 1

     elif operator == '=':
         if pruning != '':
             stack.append(pruning)
             pruning = ''
         stack.append(input_buffer[n])

     else :
         print('Error')

     if pruning != '' :
         if pruning in grammar :
             print(pruning)
             pruning= 'E'

             print('pruning \n')

     print('Stack at end is : \n', stack)
     n += 1

print(input_buffer,stack)
