with open('c_program.txt') as f:
   lines = f.readlines()
lines = [x.strip() for x in lines]
print(lines)
keywords = ['include', 'void', 'main', 'printf', 'scanf', 'stdio.h', 'conio.h' 'int', 'float', 'char', 'while', 'for', 'do', 'if', 'else']
operators = {'+', '-', '=', '*', '/', '%'}
keyword, s_char, number, error, strings, var, operator = [], [], [], [], [], [], []
string_flag = ""

for l in lines:
   word, prev = "", ""
   alphabets = list(l)
   print(alphabets)
   for a in alphabets:
      if string_flag != "":           # For strings
         if a == string_flag:
            strings.append(word)
            string_flag = ""
            word = ""
         else:
            word += a
      elif a == "'":
         string_flag = "'"
      elif a == '"':
         string_flag = '"'
      elif a.isalpha() or a == "_" or a == "." or a.isdigit():
         if prev == "alpha" or prev == "digit":
            word += a
            prev = "alpha"
         elif prev == "special" or prev == "":
            word = a
            prev = "alpha"
      elif a in operators:
         prev = "operator"
         operator.append(a)
      else:
         prev = "special"
         if word == "":
            pass
         else:
            if word in keywords:
               keyword.append(word)
            elif word[0].isdigit():
               if word.isdigit():
                  number.append(word)
               else:
                  error.append(word)
            else:
               var.append(word)
            word = ""
         s_char.append(a)
print('\nStrings', strings, '\nVariables', var, '\nKeywords', keyword, '\nSpecial characters', s_char, '\nOperators', operator, '\nNumbers', number)
