from . import base_types
import Algorithm7Code
import PublicRSAKey1

class PublicRSAKey2(base_types._BaseFieldType):

	__slots__ = ["_Algo", "_PblcKeyVal"]
	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if type(value) != auto else self.make_default("Algo")

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = None

	@property
	def PblcKeyVal(self):
		return self._PblcKeyVal

	@PblcKeyVal.setter
	def PblcKeyVal(self, value):
		self._PblcKeyVal = value if type(value) != auto else self.make_default("PblcKeyVal")

	@PblcKeyVal.deleter
	def PblcKeyVal(self):
		del self._PblcKeyVal
		self._PblcKeyVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Algo', type=Algorithm7Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblcKeyVal', type=PublicRSAKey1, min=1, max=1, mutex_group=None, array=False),
	))

