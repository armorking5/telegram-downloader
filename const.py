# Put in const.py...:
class _const:
	class ConstError(TypeError): pass
	def __setattr__(self,name,value):
		if name in self.__dict__:
			raise self.ConstError("Can't rebind const(%s)"%name)
		self.__dict__[name]=value
	def __delattr__(self,name):
		raise self.ConstError("Can't delete const(%s)"%name)
		
import sys

sys.modules[__name__]=_const()
