#Balance chemical equations
#Feb 18, 2022
#Ryan Cullen

import pytest
from equation_balancer.utils import reader, equality

a,b,c,d = reader("C8H18 + O2 -> CO2 + H2O")
equality(c,d)

pytest.main()