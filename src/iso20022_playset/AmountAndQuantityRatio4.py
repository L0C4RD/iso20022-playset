from . import base_types
from .DecimalNumber import DecimalNumber
from .ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount

class AmountAndQuantityRatio4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Qty"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

