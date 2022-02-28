from chemBal.utils import reader, solve

##test if the function returns the correct answers
def test_formation() :
  test_1 = "Al + O2 -> Al2O3"
  a,b = reader(test_1)
  assert solve(a,b) == ([4,3,2], test_1)

def test_decomposition() :
  test_2 = "CaBr2 -> Ca + Br2"
  a,b = reader(test_2)
  assert solve(a,b) == ([1,1,1], test_2)
  
def test_single_replacement() :
  test_3 = "K2S + Mg -> MgS + K"
  a,b = reader(test_3)
  assert solve(a,b) == ([1,1,1,2], test_3)
  
def test_formation_with_trailing_letter() :
  test_4 = "K + O2 -> K2O"
  a,b = reader(test_4)
  assert solve(a,b) == ([4,1,2], test_4)

def test_double_replacement() :
  test_5 = "Li2O + FeF3 -> LiF + Fe2O3"
  a,b = reader(test_5)
  assert solve(a,b) == ([3,2,6,1], test_5)
  
def test_single_replacement_with_brackets() :
  test_6 = "Cu(OH)2 + K -> KOH + Cu"
  a,b = reader(test_6)
  assert solve(a,b) == ([1,2,2,1], test_6)

def test_formation_with_brackets() :
  test_7 = "NH4 + S8 -> (NH4)2S"
  a,b = reader(test_7)
  assert solve(a,b) == ([16,1,8], test_7)

def test_high_digits() :
  test_8 = "C8H18 + O2 -> CO2 + H2O"
  a,b = reader(test_8)
  assert solve(a,b) == ([2,25,16,18], test_8)

def test_high_bracket_double_replacement() :
  test_9 = "(NH4)3PO4 + Mg(CH3COO)2 -> Mg3(PO4)2 + NH4CH3COO"
  a,b = reader(test_9)
  assert solve(a,b) == ([2,3,1,6], test_9)

def test_unnecessary_brackets() :
  test_10 = "(Mg)(OH)2 + (Fe) -> (Fe)(OH)3 + Mg"
  a,b = reader(test_10)
  assert solve(a,b) == ([3,2,2,3], test_10)