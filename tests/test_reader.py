from chemBal.utils import reader

#test if the function returns the correct answers
def test_formation() :
  test_1 = "Al + O2 -> Al2O3"
  assert reader(test_1) == ([[1,0],[0,2],[-2,-3]], test_1)

def test_decomposition() :
  test_2 = "CaBr2 -> Ca + Br2"
  assert reader(test_2) == ([[1,2],[-1,0],[0,-2]], test_2)

def test_single_replacement() :
  test_3 = "K3S + Mg -> Mg3S2 + K"
  assert reader(test_3) == ([[3,1,0],[0,0,1],[0,-2,-3],[-1,0,0]], test_3)
  
def test_formation_with_trailing_letter() :
  test_4 = "K + O2 -> K2O"
  assert reader(test_4) == ([[1,0],[0,2],[-2,-1]], test_4)

def test_double_replacement() :
  test_5 = "Li2O + FeF3 -> LiF + Fe2O3"
  assert reader(test_5) == ([[2,1,0,0],[0,0,1,3],[-1,0,0,-1],[0,-3,-2,0]], test_5)
  
def test_single_replacement_with_brackets() :
  test_6 = "Cu(OH)2 + K -> KOH + Cu"
  assert reader(test_6) == ([[1,2,2,0],[0,0,0,1],[0,-1,-1,-1],[-1,0,0,0]], test_6)

def test_formation_with_brackets() :
  test_7 = "NH4 + S8 -> (NH4)2S"
  assert reader(test_7) == ([[1,4,0],[0,0,8],[-2,-8,-1]], test_7)

def test_high_digits() :
  test_8 = "C8H18 + O2 -> CO2 + H2O"
  assert reader(test_8) == ([[8,18,0],[0,0,2],[-1,0,-2],[0,-2,-1]], test_8)

def test_high_bracket_double_replacement() :
  test_9 = "(NH4)3PO4 + Mg(CH3COO)2 -> Mg3(PO4)2 + NH4CH3COO"
  assert reader(test_9) == ([[3,12,1,4,0,0],[0,6,0,4,1,4],[0,0,-2,-8,-3,0],[-1,-7,0,-2,0,-2]], test_9)

def test_unnecessary_brackets() :
  test_10 = "(Mg)(OH)2 + (Fe) -> (Fe)(OH)3 + Mg"
  assert reader(test_10) == ([[1,2,2,0],[0,0,0,1],[0,-3,-3,-1],[-1,0,0,0]], test_10)