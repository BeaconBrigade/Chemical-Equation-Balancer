from sympy import Matrix, lcm

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
  child_parent = {}
  
  #Seperate elements by compound and letter
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
        child_elm.append(''.join([x for x in cur_elmt[0] if x.isalpha()]))
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
            child_elm.append(cur_elmt[0][:-1 * len(str(coef * int(num)))])
            elements.append(cur_elmt)
            cur_elmt = []
          else :

            #Assuming one is the number.
            cur_elmt.append(''.join([prev_letter,letter,str(coef * 1)]))
            child_elm.append(''.join([x for x in cur_elmt[0] if x.isalpha()]))
            elements.append(cur_elmt)
            cur_elmt = []
        else :

          #If it's the end of the string, assume one is the number.
          cur_elmt.append(''.join([prev_letter,letter, str(coef * 1)]))
          child_elm.append(''.join([x for x in cur_elmt[0] if x.isalpha()]))
          elements.append(cur_elmt)
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
            child_elm.append(cur_elmt[0][:-1 * len(str(coef * int(num)))])

            elements.append(cur_elmt)
            cur_elmt = []
          else :

            #Assuming the number is one.
            cur_elmt.append(''.join([letter, str(coef * 1)]))
            child_elm.append(''.join([x for x in cur_elmt[0] if x.isalpha()]))
            elements.append(cur_elmt)
            cur_elmt = []

        elif i + 1 == len(cmpnd) :

          #If it's the last character of the element, assume one is the number.
          cur_elmt.append(''.join([letter, str(coef * 1)]))
          child_elm.append(''.join([x for x in cur_elmt[0] if x.isalpha()]))
          elements.append(cur_elmt)
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
        cur_elmt = []
        
      prev_letter = letter
  
    #Keep track of the compound and its elements
    if child_elm :
      child_parent[cmpnd] = child_elm

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

  #Record all unique elements.
  unique_elements = []
  for i in reactants_elements :
    elm = []
    for j in i :
      if j.isalpha() :
        elm.append(j)
    elm = ''.join(elm)
    if elm not in unique_elements :
      unique_elements.append(elm)
  print(unique_elements)
  
  #Create blank matrix
  matrix = []
  for i in range(len(compounds) - 1) :
    matrix.append([])
    for j in unique_elements :
      matrix[i].append(0)

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

  #Find the total occurences of each element
  connected_react = ' '.join(reactants_compounds)
  total_count = {}
  current_count = {}
  for i in reactants_elements :
    j = ''.join([x for x in i if x.isalpha()])
    total_count[j] = connected_react.count(i)
    current_count[j] = 0

  #Fill in reactant side of matrix
  for i in range(len(reactants_compounds)) : 
    for t in reactants_elements :
      #Find number
      number = []
      for j in t :
        if j.isnumeric() :
          number.append(j)
      number = int(''.join(number))
      slices = -1 * len(str(number))

      #Remove number to search for the unique element
      elm = t[:slices]

      #Find the correct element
      next = connected_react.find(elm)
      n = current_count[elm] + 1
      while next >= 0 and n > 1:
        next = connected_react.find(elm, next + 1)
        n -= 1

      print(f"Next: {next}")

      #If the element is the correct element
      if t in reactants_compounds[i][next:] :  
        #Add number to matrix if it's a part of this compound
        if elm in child_parent[reactants_compounds[i]] :
          #Add if we haven't exceeded the limit of expected elements
          if current_count[elm] < total_count[elm] :
            matrix[i][unique_elements.index(elm)] += number
            current_count[elm] += 1

  #Find the total occurences of each element
  connected_result = ' '.join(resultants_compounds)
  total_count = {}
  current_count = {}
  for i in resultants_elements :
    j = ''.join([x for x in i if x.isalpha()])
    total_count[j] = connected_result.count(i)
    current_count[j] = 0

  #Resultant side of matrix
  for i in range(len(resultants_compounds)) :
    for t in resultants_elements :
      #Find number
      number = []
      for j in t :
        if j.isnumeric() :
          number.append(j)
      number = -1 * int(''.join(number))
      slices = -1 * (len(str(number)) - 1)

      #Remove number to search for the unique element
      elm = t[:slices]

      #Find the correct element
      next = connected_result.find(elm)
      n = current_count[elm] + 1
      while next >= 0 and n > 1:
        next = connected_result.find(elm, next+len(elm))
        n -= 1

      #If the element is the correct element
      if t in resultants_compounds[i][next:] :  
        #Add number to matrix if it's a part of this compound
        if elm in child_parent[resultants_compounds[i]] :
          #Add if we haven't exceeded the limit of expected elements
          if current_count[elm] < total_count[elm] :
            print(f"adding {number}") 
            matrix[i + len(reactants_compounds)][unique_elements.index(elm)] += number
            current_count[elm] += 1
    
  print(matrix)
  
  return matrix, unique_elements, reactants_compounds, resultants_compounds, equation

#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#

def balancer(matrix, unique, reactants, products, equation) :
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