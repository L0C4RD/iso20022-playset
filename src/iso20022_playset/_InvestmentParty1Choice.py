from . import base_types
from ._Max50Text import Max50Text
from ._PersonIdentification12 import PersonIdentification12

class InvestmentParty1Choice(base_types._BaseFieldType):

	__slots__ = ["_Algo", "_Prsn"]
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
	def Prsn(self):
		return self._Prsn

	@Prsn.setter
	def Prsn(self, value):
		self._Prsn = value if type(value) != base_types.auto else self.make_default("Prsn")

	@Prsn.deleter
	def Prsn(self):
		del self._Prsn
		self._Prsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Algo', type=Max50Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prsn', type=PersonIdentification12, min=0, max=1, mutex_group=1, array=False),
	))

