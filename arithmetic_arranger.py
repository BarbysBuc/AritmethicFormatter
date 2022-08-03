def arithmetic_arranger(problems, res = False):
#Initializing the future printing  
  top = ''
  bottom = ''
  line = ''
  result = ''  
#Checking limit of problems
  if len(problems) > 5:
    return('Error: Too many problems.')
    

#Checking operators and operands
  for p in problems:
    a = p.split()[0]
    op = p.split()[1]
    b = p.split()[2]

    if op == '*' or op == '/':
      return("Error: Operator must be '+' or '-'.")
      
    if not a.isdigit() or not b.isdigit():
      return('Error: Numbers must only contain digits.')
      
    if len(a) > 4 or len(b) > 4:
      return('Error: Numbers cannot be more than four digits.')
      

  # Distance calculating for printing
    dist = max(len(a), len(b)) + 2
  # Getting solve for each problem
    if op == '+':
      total = int(a) + int(b)
    elif op == '-':
      total = int(a) - int(b)
  
  # Creating format
    b = op + b.rjust(dist-1)  
    if p  == problems[-1]:  
      top += a.rjust(dist)+ '\n'
      bottom += b + '\n'
      line += dist * '-' 
      result += str(total).rjust(dist)

    else:
      
      top += a.rjust(dist) + '    '
      bottom += b + '    '
      line += dist * '-'+ '    '
      result += str(total).rjust(dist) + '    '

  if res:
    return top + bottom +  line + '\n' + result
  else:
    return top + bottom + line