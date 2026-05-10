from . import base_types
from ._Parameter14 import Parameter14
from ._Algorithm13Code import Algorithm13Code

class AlgorithmIdentification28(base_types._BaseFieldType):

	__slots__ = ["_Param", "_Algo"]
	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if type(value) != base_types.auto else self.make_default("Algo")

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = None

	@property
	def Param(self):
		return self._Param

	@Param.setter
	def Param(self, value):
		self._Param = value if type(value) != base_types.auto else self.make_default("Param")

	@Param.deleter
	def Param(self):
		del self._Param
		self._Param = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Algo', type=Algorithm13Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Param', type=Parameter14, min=0, max=1, mutex_group=None, array=False),
	))

