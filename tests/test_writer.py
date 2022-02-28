from equation_balancer.utils import balance

##test if the function returns the correct answers
def test_formation() :
  test_1 = "Al + O2 -> Al2O3"
  assert balance(test_1) == "4Al + 3O2 -> 2Al2O3"

def test_decomposition() :
  test_2 = "CaBr2 -> Ca + Br2"
  assert balance(test_2) == "CaBr2 -> Ca + Br2"
  
def test_single_replacement() :
  test_3 = "K2S + Mg -> MgS + K"
  assert balance(test_3) == "K2S + Mg -> MgS + 2K"
  
def test_formation_with_trailing_letter() :
  test_4 = "K + O2 -> K2O"
  assert balance(test_4) == "4K + O2 -> 2K2O"

def test_double_replacement() :
  test_5 = "Li2O + FeF3 -> LiF + Fe2O3"
  assert balance(test_5) == "3Li2O + 2FeF3 -> 6LiF + Fe2O3"
  
def test_single_replacement_with_brackets() :
  test_6 = "Cu(OH)2 + K -> KOH + Cu"
  assert balance(test_6) == "Cu(OH)2 + 2K -> 2KOH + Cu"

def test_formation_with_brackets() :
  test_7 = "NH4 + S8 -> (NH4)2S"
  assert balance(test_7) == "16NH4 + S8 -> 8(NH4)2S"

def test_high_digits() :
  test_8 = "C8H18 + O2 -> CO2 + H2O"
  assert balance(test_8) == "2C8H18 + 25O2 -> 16CO2 + 18H2O"

def test_high_bracket_double_replacement() :
  test_9 = "(NH4)3PO4 + Mg(CH3COO)2 -> Mg3(PO4)2 + NH4CH3COO"
  assert balance(test_9) == "2(NH4)3PO4 + 3Mg(CH3COO)2 -> Mg3(PO4)2 + 6NH4CH3COO"

def test_unnecessary_brackets() :
  test_10 = "(Mg)(OH)2 + (Fe) -> (Fe)(OH)3 + Mg"
  assert balance(test_10) == "3(Mg)(OH)2 + 2(Fe) -> 2(Fe)(OH)3 + 3Mg"