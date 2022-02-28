#Balance chemical equations
#Feb 18, 2022
#Ryan Cullen

import pytest
from chemBal.utils import balance
import colorama as clr

x = input("Input equation: ")

if not x :
  pytest.main()
else :
  print(f"{clr.Fore.PURPLE}{balance(x)}")