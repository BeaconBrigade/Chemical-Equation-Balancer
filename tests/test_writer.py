from chemBal.utils import balance

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

def test_formation_1() :
  assert balance('Ca + O2 -> CaO') == "2Ca + O2 -> 2CaO"

def test_formation_2() :
  assert balance("Sc + O2 -> Sc2O3") == "4Sc + 3O2 -> 2Sc2O3"

def test_formation_3() :
  assert balance("Na + Cl2 -> NaCl") == "2Na + Cl2 -> 2NaCl"

def test_formation_4() :
  assert balance("S8 + O2 -> SO2") == "S8 + 8O2 -> 8SO2"

def test_formation_5() :
  assert balance("N2O5 + H2O -> HNO3") == "N2O5 + H2O -> 2HNO3"

def test_formation_6() :
  assert balance("Al + Br2 -> AlBr3") == "2Al + 3Br2 -> 2AlBr3"

def test_formation_7() :
  assert balance("C + O2 -> CO") == "2C + O2 -> 2CO"

def test_formation_8() :
  assert balance("Li + P4 -> Li3P") == "12Li + P4 -> 4Li3P"

def test_formation_9() :
  assert balance("K + Cl2 -> KCl") == "2K + Cl2 -> 2KCl"

def test_formation_10() :
  assert balance("Na + S8 -> Na2S") == "16Na + S8 -> 8Na2S"

def test_decomposition_1() :
  assert balance("HgO -> Hg + O2") == "2HgO -> 2Hg + O2"

def test_decomposition_2() :
  assert balance("NH3 -> N2 + H2") == "2NH3 -> N2 + 3H2"

def test_decomposition_3() :
  assert balance("Ag2O -> Ag + O2") == "2Ag2O -> 4Ag + O2"

def test_decomposition_4() :
  assert balance("NaClO + HCl -> Cl2 + NaCl + H2O") == "NaClO + 2HCl -> Cl2 + NaCl + H2O"

def test_decomposition_5() :
  assert balance("H2SO4 + NaHCO3 -> Na2SO4 + CO2 + H2O") == "H2SO4 + 2NaHCO3 -> Na2SO4 + 2CO2 + 2H2O"

def test_decomposition_6() :
  assert balance("NaClO3 -> NaCl + O2") == "2NaClO3 -> 2NaCl + 3O2"

def test_decomposition_7() :
  assert balance("Ag2S -> Ag + S8") == "8Ag2S -> 16Ag + S8"

def test_decomposition_8() :
  assert balance("Fe2O3 -> Fe + O2") == "2Fe2O3 -> 4Fe + 3O2"

def test_decomposition_9() :
  assert balance("KHCO3 -> K2CO3 + H2O + CO2") == "2KHCO3 -> K2CO3 + H2O + CO2"

def test_decomposition_10() :
  assert balance("KClO3 -> KCl + O2") == "2KClO3 -> 2KCl + 3O2"

def test_single_replacement_1() :
  assert balance("Cu + AgNO3 -> Ag + Cu(NO3)2") == "Cu + 2AgNO3 -> 2Ag + Cu(NO3)2"

def test_single_replacement_2() :
  assert balance("Al + H2SO4 -> Al2(SO4)3 + H2") == "2Al + 3H2SO4 -> Al2(SO4)3 + 3H2"

def test_single_replacement_3() :
  assert balance("Cl2 + KI -> KCl + I2") == "Cl2 + 2KI -> 2KCl + I2"

def test_single_replacement_4() :
  assert balance("Cu + FeSO4 -> Cu2SO4 + Fe") == "2Cu + FeSO4 -> Cu2SO4 + Fe"

def test_single_replacement_5() :
  assert balance("Li + KOH -> H2 + LiOH") == "2Li + 2KOH -> H2 + 2LiOH"

def test_single_replacement_6() :
  assert balance("Zn + Pb(NO3)4 -> Zn(NO3)2 + Pb") == "2Zn + Pb(NO3)4 -> 2Zn(NO3)2 + Pb"

def test_single_replacement_7() :
  assert balance("Br2 + NaI -> I2 + NaBr") == "Br2 + 2NaI -> I2 + 2NaBr"

def test_single_replacement_8() :
  assert balance("Al + Cu(NO3)2 -> Cu + Al(NO3)3") == "2Al + 3Cu(NO3)2 -> 3Cu + 2Al(NO3)3"

def test_single_replacement_9() :
  assert balance("Li + AlBr3 -> LiBr + Al") == "3Li + AlBr3 -> 3LiBr + Al"

def test_single_replacement_10() :
  assert balance("Na + KOH -> NaOH + H2") == "2Na + 2KOH -> 2NaOH + H2"

