from sympy import Matrix, lcm

def addMatrix(matrix, cmpnd, compounds, element, unique, side) :
  """Add to the matrix. Also add to unique elements if needed."""

  updated_matrix = matrix
  new_unique = unique
  pureComp = [x for x in compounds if not '->' in x]

  #Split element and number
  elm = ''.join([x for x in element if x.isalpha()])

  try :
    num = int(''.join([x for x in element if x.isnumeric()]))
  except ValueError :
    num = 1

  #Add the element if it's not already there.
  if elm not in new_unique :
    new_unique.append(elm)
    for i in range(len(updated_matrix)) :
      updated_matrix[i].append(0)

  #Add to the matrix
 
  updated_matrix[pureComp.index(cmpnd)][unique.index(elm)] += (num * side)

  return (updated_matrix, new_unique)

#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#

def reader(equation) :
  """Convert input into elements that the computer can balance."""

  #Variables
  reactants_compounds = []
  reactants_elements = []
  resultants_compounds = []
  resultants_elements = []

  #Seperate all of the compounds and leave the -> sign in.
  compounds = equation.split(' ')
  compounds = [x for x in compounds if not x == '+']

  #Find each element and its amount
  is_reactant = True
  elements = []

  #Create blank matrix
  matrix = []
  for i in range(len(compounds) - 1) :
    matrix.append([])
  
  #Seperate elements by compound and letter
  unique_elements = []
  side = 1
  for cmpnd in compounds :
    
    #List for typing element
    cur_elmt = []

    #For writing two letter elements and equals signs
    prev_letter = ''

    #Keep track of what compound the element belongs to
    child_elm = []

    #Coefficient for brackets. Default is one.
    coef = 1
    
    for i, letter in enumerate(cmpnd):

      #Alone single element
      if len(cmpnd) == 1 :
        cur_elmt = [''.join([cmpnd, str(coef * 1)])]
        elements.append(cur_elmt)
        matrix, unique_elements = addMatrix(matrix, cmpnd, compounds, cur_elmt[0], unique_elements, side)
        break

      #Two letter element
      elif letter.islower() :
        
        if i + 1 != len(cmpnd) :
          
          #If this isn't the end of the string.
          if cmpnd[i + 1].isnumeric() :

            #Find numbers
            num = []
            for p in cmpnd[i + 1:] :
              if p.isnumeric() :
                num.append(p)
              else :
                break
            num = ''.join(num)

            #Using given number.
            cur_elmt.append(''.join([prev_letter,letter,str(coef * int(num))]))
            elements.append(cur_elmt)
            matrix, unique_elements = addMatrix(matrix, cmpnd, compounds, cur_elmt[0], unique_elements, side)
            cur_elmt = []
          else :

            #Assuming one is the number.
            cur_elmt.append(''.join([prev_letter,letter,str(coef * 1)]))
            elements.append(cur_elmt)
            matrix, unique_elements = addMatrix(matrix, cmpnd, compounds, cur_elmt[0], unique_elements, side)
            cur_elmt = []
        else :

          #If it's the end of the string, assume one is the number.
          cur_elmt.append(''.join([prev_letter,letter, str(coef * 1)]))
          elements.append(cur_elmt)
          matrix, unique_elements = addMatrix(matrix, cmpnd, compounds, cur_elmt[0], unique_elements, side)
          cur_elmt = []
      
      #Single letter element
      elif letter.isupper() :
        
        #If this isn't the end of the string and the next letter isn't a lower 
        #case (meaning it will be a two letter element to be handled by the 
        #.islower() elif statement)
        if i + 1 != len(cmpnd) and (not (cmpnd[i + 1].islower() and cmpnd[i + 1].isalpha())) :
          
          if cmpnd[i + 1].isnumeric() :  

            #Can't use a break, so this code will take every number of every
            #element. So sad :(
            #num = ''.join([x for x in cmpnd[i:] if x.isnumeric()])
            
            #This ugly thing can use breaks so...
            num = []
            for r in cmpnd[i + 1:] :
              if r.isnumeric() :
                num.append(r)
              else :
                break
            num = ''.join(num)

            #Using given number.
            cur_elmt.append(''.join([letter,str(coef * int(num))]))
            elements.append(cur_elmt)
            matrix, unique_elements = addMatrix(matrix, cmpnd, compounds, cur_elmt[0], unique_elements, side)
            cur_elmt = []
          else :

            #Assuming the number is one.
            cur_elmt.append(''.join([letter, str(coef * 1)]))
            elements.append(cur_elmt)
            matrix, unique_elements = addMatrix(matrix, cmpnd, compounds, cur_elmt[0], unique_elements, side)
            cur_elmt = []

        elif i + 1 == len(cmpnd) :

          #If it's the last character of the element, assume one is the number.
          cur_elmt.append(''.join([letter, str(coef * 1)]))
          elements.append(cur_elmt)
          matrix, unique_elements = addMatrix(matrix, cmpnd, compounds, cur_elmt[0], unique_elements, side)
          cur_elmt = []
      
      #If there's a bracket, set the coefficient to the number following
      elif letter == '(' :

        try :
          coef = int(cmpnd[cmpnd.index(')') + 1])
        #If the character after the end of the string isn't a number, or is the
        #end of the string, set the coefficient to 1 
        except :
          coef = 1

      #At the end of the bracket, reset the coefficient to one.
      elif letter == ')' :
        coef = 1

      #Equals sign
      elif letter == ">" and prev_letter == "-":
        cur_elmt.append(''.join([prev_letter,letter]))
        elements.append(cur_elmt)
        side = -1
        cur_elmt = []
        
      prev_letter = letter

  #Seperate elements into reactants and resultants as elements
  is_reactant = True
  for i in elements :
    
    if i[0] == '->' :
      is_reactant = False

    #Before equals.
    if is_reactant :
      reactants_elements.append(i[0])
    #After equals
    else :
      resultants_elements.append(i[0])

  #Done with the equals sign
  if '->' in resultants_elements :
    resultants_elements.remove('->')
  
  #Seperate all of the compounds to the reactants or resultants as compounds
  is_reactant = True
  for i in compounds :
    #Determine which side of the equation it's on
    if i == "->" :
      is_reactant = False
    
    #Add to the reactant or resultant
    if is_reactant:
      reactants_compounds.append(i)
    else:
      resultants_compounds.append(i)
  resultants_compounds.remove('->')
  
  return matrix, unique_elements, reactants_compounds, resultants_compounds, equation

#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#

def solve(matrix, unique, reactants, products, equation) :
  """Balance input on both sides of the equation."""

  #Transpose the matrix so that each row is row is the amounts of an element
  sym_matrix = Matrix(matrix)
  sym_matrix = sym_matrix.transpose()
  print(f"Transposed matrix: {sym_matrix}")

  #Find nullspace
  solution = sym_matrix.nullspace()[0]
  
  print(f"Solution: {solution}")

  #Convert fractions to integer coefficients
  multiple = lcm([x.q for x in solution])
  print(f"Multiple: {multiple}")

  solution = solution * multiple.numerator / multiple.denominator
  print(f"Coefficients: {solution}")

  return solution, equation

#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#

def writer(solution, equation) :
  """Write balanced equation back into a readable format to be printed out."""
  #use .join(" + " or " -> ") to create the equation
  
  pass