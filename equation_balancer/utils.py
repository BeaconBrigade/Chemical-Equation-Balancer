from equation_balancer.dictlist import Dictlist as dictL

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
        child_elm.append(cur_elmt[0][:-1])
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
            child_elm.append(cur_elmt[0][:-1])
            elements.append(cur_elmt)
            cur_elmt = []
        else :

          #If it's the end of the string, assume one is the number.
          cur_elmt.append(''.join([prev_letter,letter, str(coef * 1)]))
          child_elm.append(cur_elmt[0][:-1])
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
            child_elm.append(cur_elmt[0][:-1])
            elements.append(cur_elmt)
            cur_elmt = []

        elif i + 1 == len(cmpnd) :

          #If it's the last character of the element, assume one is the number.
          cur_elmt.append(''.join([letter, str(coef * 1)]))
          child_elm.append(cur_elmt[0][:-1])
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
    if i not in unique_elements :
      unique_elements.append(i)

  #Create blank matrix
  matrix = []
  for i in range(len(compounds)) :
    matrix.append([])
    for j in unique_elements :
      matrix[i].append(0)

  print(matrix)

  
  
  #Create dictionaries that store the element and the amount
  react_elm = dictL()
  result_elm = dictL()

  for t in reactants_elements :
    number = []
    for j in t :
      if j.isnumeric() :
        number.append(j)
    number = ''.join(number)
    slices = -1 * len(number)
    react_elm[t[:slices]] = int(number)

  for q in resultants_elements :
    number = []
    for z in q :
      if z.isnumeric() :
        number.append(z)
    number = ''.join(number)
    slices = -1 * len(number)
    result_elm[q[:slices]] = int(number)
    
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

  #Remove the equals sign
  resultants_compounds.remove('->')

  #Dictionaries of the compound to element
  react_comp = {x : child_parent[x] for x in reactants_compounds}
  result_comp = {x : child_parent[x] for x in resultants_compounds}
  print(react_elm)
  print(result_elm)
  return (react_comp, result_comp, react_elm, result_elm)

#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#

def equality(rct_elm, rslt_elm) :
  """Check if the number of each element is the same on both sides."""

  react = {}
  result = {}

  #Create new dict with summed repeats
  for key, value in rct_elm.items() :
    react[key] = sum(value)

  #Add the resultants duplicates together
  for key, value in rslt_elm.items() :
    result[key] = sum(value)

  inequalities = {}

  react_key, react_value, = list(react.keys()), list(react.values())

  #Check for equality and record which elements aren't equal
  for i in range(len(react_key)) :
    
    if react_value[i] > result[react_key[i]] :
      inequalities[react_key[i]] = 1
    elif react_value[i] < result[react_key[i]] :
      inequalities[react_key[i]] = 0

  return inequalities

#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#

def balancer(rct_cmp, rslt_comp, rct_elm, rslt_elm) :
  """Balance input on both sides of the equation."""

  #Store old versions for reverting
  old = (rct_elm,rslt_elm,rct_comp,rslt_comp)

  #Start coefficient
  coef = 2

  react = {x : 1 for x in rct_cmp}
  result = {x : 1 for x in rslt_cmp}
  
  #Repeat until the equation is balanced
  while True :
    is_equal = equality(rct_elm,rslt_elm)
    
    #Equation is balanced
    if not is_equal :
      return react, result

    #Find a way to try every combination of coefficients in 
    #ascending order checking equality after each change.

    

#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////////////#

def writer(equation) :
  """Write balanced equation back into a readable format to be printed out."""
  #use .join(" + " or " -> ") to create the equation
  
  pass