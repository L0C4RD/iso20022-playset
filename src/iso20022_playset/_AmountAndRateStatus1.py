from . import base_types
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._RateStatus1Code import RateStatus1Code

class AmountAndRateStatus1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_RateSts"]
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

	@property
	def RateSts(self):
		return self._RateSts

	@RateSts.setter
	def RateSts(self, value):
		self._RateSts = value if type(value) != base_types.auto else self.make_default("RateSts")

	@RateSts.deleter
	def RateSts(self):
		del self._RateSts
		self._RateSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateSts', type=RateStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

