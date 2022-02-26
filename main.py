#Balance chemical equations
#Feb 18, 2022
#Ryan Cullen

import pytest
from equation_balancer.utils import reader

reader("C8H18 + O2 -> CO2 + H2O")

reader("(NH4)3PO4 + Mg(CH3COO)2 -> Mg3(PO4)2 + NH4CH3COO")

#pytest.main()