#!/usr/bin/env python
import time


# special methods: __init__, __repr__, __add__, __len__, __call___, __eq__, __order__, __unsafe_has___, __frozen___
# dataclass() decarator: used to add generated special methods to class

class Polynomial:
	# python class constructor
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial(*{!r})'.format(self.coeffs)
 
	def __add__(self, other):
		return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

	def __len__(self):
		return len(self.coeffs)

	def __call__(self):
		pass
   		
	#pass # substitues using comment as place holder 

p1 = Polynomial(1, 2, 3) # x^2 + 2x + 3
p2 = Polynomial(3, 4, 3) # 3x^2 + 4x + 3
print(p1,'\n',p2)
time.sleep(3)