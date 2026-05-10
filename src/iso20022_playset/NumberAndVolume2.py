from . import base_types
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .DecimalNumberFraction5 import DecimalNumberFraction5

class NumberAndVolume2(base_types._BaseFieldType):

	__slots__ = ["_Vol", "_Nb"]
	@property
	def Vol(self):
		return self._Vol

	@Vol.setter
	def Vol(self, value):
		self._Vol = value if type(value) != base_types.auto else self.make_default("Vol")

	@Vol.deleter
	def Vol(self):
		del self._Vol
		self._Vol = None

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != base_types.auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Vol', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=DecimalNumberFraction5, min=1, max=1, mutex_group=None, array=False),
	))

