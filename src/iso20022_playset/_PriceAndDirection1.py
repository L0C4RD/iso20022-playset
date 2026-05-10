from . import base_types
from ._PlusOrMinusIndicator import PlusOrMinusIndicator
from ._ActiveOrHistoricCurrencyAnd13DecimalAmount import ActiveOrHistoricCurrencyAnd13DecimalAmount

class PriceAndDirection1(base_types._BaseFieldType):

	__slots__ = ["_Val", "_Sgn"]
	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if type(value) != base_types.auto else self.make_default("Sgn")

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
	))

