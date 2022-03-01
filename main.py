#Balance chemical equations
#Feb 18, 2022
#Ryan Cullen

import pytest
from chemBal.utils import balance

x = input("Input equation: ")

if not x :
  pytest.main()
else :
  print(balance(x))
