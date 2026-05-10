from . import base_types
from ._CardIndividualTransaction2 import CardIndividualTransaction2
from ._CardAggregated2 import CardAggregated2

class CardTransaction3Choice(base_types._BaseFieldType):

	__slots__ = ["_Aggtd", "_Indv"]
	@property
	def Aggtd(self):
		return self._Aggtd

	@Aggtd.setter
	def Aggtd(self, value):
		self._Aggtd = value if type(value) != base_types.auto else self.make_default("Aggtd")

	@Aggtd.deleter
	def Aggtd(self):
		del self._Aggtd
		self._Aggtd = None

	@property
	def Indv(self):
		return self._Indv

	@Indv.setter
	def Indv(self, value):
		self._Indv = value if type(value) != base_types.auto else self.make_default("Indv")

	@Indv.deleter
	def Indv(self):
		del self._Indv
		self._Indv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Aggtd', type=CardAggregated2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Indv', type=CardIndividualTransaction2, min=0, max=1, mutex_group=1, array=False),
	))

