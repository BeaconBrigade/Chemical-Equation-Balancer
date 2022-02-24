from equation_balancer.utils import reader

test_1 = "Al + O2 -> Al2O3"
test_2 = "CaBr2 -> Ca + Br2"
test_3 = "K3S + Mg -> Mg3S2 + K"
test_4 = "K + O -> K2O"
test_5 = "Li2O + FeF3 -> LiF + Fe2O3"
test_6 = "Cu(OH)2 + K -> KOH + Cu"
test_7 = "NH4 + S8 -> (NH4)2S"
test_8 = "C8H18 + O2 -> CO2 + H2O"
test_9 = "(NH4)3PO4 + Mg(CH3COO)2 -> Mg3(PO4)2 + NH4CH3COO"

#test if the function returns the correct answers
def test_formation() :
  assert reader(test_1) == ({"Al": ["Al"], "O2":["O"]}, {"Al2O3": ["Al", "O"]}, {"Al": [1],"O":[2]}, {"Al": [2], "O": [3]})

def test_decomposition() :
  assert reader(test_2) == ({"CaBr2": ["Ca", "Br"]},{"Ca": ["Ca"],"Br2": ["Br"]},{"Ca": [1],"Br": [2]},{"Ca": [1],"Br": [2]})

def test_single_replacement() :
  assert reader(test_3) == ({"K3S": ["K","S"],"Mg":["Mg"]},{"Mg3S2": ["Mg","S"],"K": ["K"]},{"K":[3],"S":[1],"Mg":[1]},{"Mg":[3],"S":[2],"K":[1]})

def test_formation_with_trailing_letter() :
  assert reader(test_4) == ({"K":["K"], "O":["O"]},{"K2O":["K","O"]},{"K":[1], "O":[1]},{"K":[2], "O":[1]})

def test_double_replacement() :
  assert reader(test_5) == ({"Li2O":["Li","O"],"FeF3":["Fe","F"]},{"LiF":["Li","F"],"Fe2O3":["Fe","O"]},{"Li":[2],"O":[1],"Fe":[1],"F":[3]},{"Li":[1],"F":[1],"Fe":[2],"O":[3]})

def test_single_replacement_with_brackets() :
  assert reader(test_6) == ({"Cu(OH)2":["Cu","O","H"],"K":["K"]},{"KOH":["K","O","H"],"Cu":["Cu"]},{"Cu":[1],"O":[2],"H":[2],"K":[1]},{"K":[1],"O":[1],"H":[1],"Cu":[1]})

def test_formation_with_brackets() :
  assert reader(test_7) == ({"NH4":["N","H"],"S8":["S"]},{"(NH4)2S":["N","H","S"]},{"N":[1],"H":[4],"S":[8]},{"N":[2],"H":[8],"S":[1]})

def test_high_digits() :
  assert reader(test_8) == ({"C8H18":["C","H"],"O2":["O"]},{"CO2":["C","O"],"H2O":["H","O"]},{"C":[8],"H":[18],"O":[2]},{"C":[1],"O":[2,1],"H":[2]})

def test_high_bracket_double_replacement() :
  assert reader(test_9) == ({"(NH4)3PO4":["N","H","P","O"], "Mg(CH3COO)2":["Mg","C","H","C","O","O"]},{"Mg3(PO4)2":["Mg","P","O"],"NH4CH3COO":["N","H","C","H","C","O","O"]},{"N":[3],"H":[12,6],"P":[1],"O":[4,2,2],"Mg":[1],"C":[2,2]},{ "Mg":[3],"P":[2],"O":[8,1,1],"N":[1],"H":[4,3],"C":[1,1]})
 