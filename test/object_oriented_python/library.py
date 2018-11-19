# library.py 

class Base: 
	def foo(self):
		return 'foo'

old_bc = __build_class__
def my_bc(*a, **kw):
	print('my buildclass_>', )
	return old_bc(*a, **kw)

import builtins
builtins.__build_class__ = my_bc