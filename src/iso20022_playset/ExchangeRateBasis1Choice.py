from . import base_types
from .ExchangeRateBasis1 import ExchangeRateBasis1
from .Max52Text import Max52Text

class ExchangeRateBasis1Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_CcyPair"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def CcyPair(self):
		return self._CcyPair

	@CcyPair.setter
	def CcyPair(self, value):
		self._CcyPair = value if type(value) != base_types.auto else self.make_default("CcyPair")

	@CcyPair.deleter
	def CcyPair(self):
		del self._CcyPair
		self._CcyPair = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CcyPair', type=ExchangeRateBasis1, min=0, max=1, mutex_group=1, array=False),
	))

