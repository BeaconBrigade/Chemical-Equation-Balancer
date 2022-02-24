from equation_balancer.utils import equality, reader

test_1 = "Al + O2 -> Al2O3"
test_2 = "CaBr2 -> Ca + Br2"
test_3 = "K3S + Mg -> Mg3S2 + K"
test_4 = "K + O -> K2O"
test_5 = "Li2O + FeF3 -> LiF + Fe2O3"
test_6 = "Cu(OH)2 + K -> KOH + Cu"
test_7 = "NH4 + S8 -> (NH4)2S"
test_8 = "C8H18 + O2 -> CO2 + H2O"
test_9 = "(NH4)3PO4 + Mg(CH3COO)2 -> Mg3(PO4)2 + NH4CH3COO"

def test_formation() :
  info = reader(test_1)
  assert equality(info[2],info[3]) == {"Al":0,"O":0}

def test_decomposition() :
  info = reader(test_2)
  assert equality(info[2],info[3]) == {}
  
def test_single_replacement() :
  info = reader(test_3)
  assert equality(info[2],info[3]) == {"K":1,"S":0,"Mg":0}

def test_formation_with_trailing_element() :
  info = reader(test_4)
  assert equality(info[2],info[3]) == {"K":0}

def test_double_replacement() :
  info = reader(test_5)
  assert equality(info[2],info[3]) == {"Li":1,"O":0,"Fe":0,"F":1}

def test_brackets() :
  info = reader(test_6)
  assert equality(info[2],info[3]) == {"O":1,"H":1}

def test_other_brackets() :
  info = reader(test_7)
  assert equality(info[2],info[3]) == {"N":0,"H":0,"S":1}

def test_high_numbers() :
  info = reader(test_8)
  assert equality(info[2],info[3]) == {"C":1,"H":1,"O":0}

def test_brackets_and_long_compounds() :
  info = reader(test_9)
  assert equality(info[2],info[3]) == {"N":1,"H":1,"P":0,"O":0,"Mg":0,"C":1}
