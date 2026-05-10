from . import base_types
from .Algorithm26Code import Algorithm26Code

class AlgorithmIdentification36(base_types._BaseFieldType):

	__slots__ = ["_Algo"]
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
		base_types.FieldEntry(name='Algo', type=Algorithm26Code, min=1, max=1, mutex_group=None, array=False),
	))

