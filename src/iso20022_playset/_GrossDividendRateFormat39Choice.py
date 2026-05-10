from . import base_types
from ._AmountAndRateStatus2 import AmountAndRateStatus2
from ._RateTypeAndAmountAndStatus59 import RateTypeAndAmountAndStatus59
from ._RestrictedFINActiveCurrencyAnd13DecimalAmount import RestrictedFINActiveCurrencyAnd13DecimalAmount

class GrossDividendRateFormat39Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtAndRateSts", "_RateTpAndAmtAndRateSts"]
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
	def AmtAndRateSts(self):
		return self._AmtAndRateSts

	@AmtAndRateSts.setter
	def AmtAndRateSts(self, value):
		self._AmtAndRateSts = value if type(value) != base_types.auto else self.make_default("AmtAndRateSts")

	@AmtAndRateSts.deleter
	def AmtAndRateSts(self):
		del self._AmtAndRateSts
		self._AmtAndRateSts = None

	@property
	def RateTpAndAmtAndRateSts(self):
		return self._RateTpAndAmtAndRateSts

	@RateTpAndAmtAndRateSts.setter
	def RateTpAndAmtAndRateSts(self, value):
		self._RateTpAndAmtAndRateSts = value if type(value) != base_types.auto else self.make_default("RateTpAndAmtAndRateSts")

	@RateTpAndAmtAndRateSts.deleter
	def RateTpAndAmtAndRateSts(self):
		del self._RateTpAndAmtAndRateSts
		self._RateTpAndAmtAndRateSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtAndRateSts', type=AmountAndRateStatus2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAndAmtAndRateSts', type=RateTypeAndAmountAndStatus59, min=0, max=1, mutex_group=1, array=False),
	))

