from . import base_types
from ._DigitalTokenAmount3 import DigitalTokenAmount3
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class CurrencyOrDigitalTokenAmount2Choice(base_types._BaseFieldType):

	__slots__ = ["_DgtlTknAmt", "_Amt"]
	@property
	def DgtlTknAmt(self):
		return self._DgtlTknAmt

	@DgtlTknAmt.setter
	def DgtlTknAmt(self, value):
		self._DgtlTknAmt = value if type(value) != base_types.auto else self.make_default("DgtlTknAmt")

	@DgtlTknAmt.deleter
	def DgtlTknAmt(self):
		del self._DgtlTknAmt
		self._DgtlTknAmt = None

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
		base_types.FieldEntry(name='DgtlTknAmt', type=DigitalTokenAmount3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))

