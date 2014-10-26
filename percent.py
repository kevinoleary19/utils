#!/usr/bin/env python
import sys
from decimal import Decimal
if __name__== "__main__":
	old = Decimal(int(sys.argv[1]))
	new = Decimal(int(sys.argv[2]))
	change =  int(100 * (new - old) / old)
	if change > 0:
		print change,'% increase'
	elif change < 0: 
		print abs(change),'% decrease'
	elif change == 0:
		print 'no change'
	
