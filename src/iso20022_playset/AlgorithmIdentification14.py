from . import base_types
import Parameter6
import Algorithm15Code

class AlgorithmIdentification14(base_types._BaseFieldType):

	__slots__ = ["_Param", "_Algo"]
	@property
	def Param(self):
		return self._Param

	@Param.setter
	def Param(self, value):
		self._Param = value if type(value) != auto else self.make_default("Param")

	@Param.deleter
	def Param(self):
		del self._Param
		self._Param = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Param', type=Parameter6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Algo', type=Algorithm15Code, min=1, max=1, mutex_group=None, array=False),
	))

