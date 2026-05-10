from . import base_types
from ._ActiveOrHistoricCurrencyAnd13DecimalAmount import ActiveOrHistoricCurrencyAnd13DecimalAmount

class PriceValue5(base_types._BaseFieldType):

	__slots__ = ["_Amt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
	))

