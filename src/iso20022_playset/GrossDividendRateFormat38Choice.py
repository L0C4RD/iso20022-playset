from . import base_types
import RateTypeAndAmountAndStatus57
import AmountAndRateStatus1
import ActiveCurrencyAnd13DecimalAmount
import RateType13Code

class GrossDividendRateFormat38Choice(base_types._BaseFieldType):

	__slots__ = ["_NotSpcfdRate", "_RateTpAndAmtAndRateSts", "_Amt", "_AmtAndRateSts"]
	@property
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if type(value) != auto else self.make_default("NotSpcfdRate")

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = None

	@property
	def RateTpAndAmtAndRateSts(self):
		return self._RateTpAndAmtAndRateSts

	@RateTpAndAmtAndRateSts.setter
	def RateTpAndAmtAndRateSts(self, value):
		self._RateTpAndAmtAndRateSts = value if type(value) != auto else self.make_default("RateTpAndAmtAndRateSts")

	@RateTpAndAmtAndRateSts.deleter
	def RateTpAndAmtAndRateSts(self):
		del self._RateTpAndAmtAndRateSts
		self._RateTpAndAmtAndRateSts = None

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
	def AmtAndRateSts(self):
		return self._AmtAndRateSts

	@AmtAndRateSts.setter
	def AmtAndRateSts(self, value):
		self._AmtAndRateSts = value if type(value) != auto else self.make_default("AmtAndRateSts")

	@AmtAndRateSts.deleter
	def AmtAndRateSts(self):
		del self._AmtAndRateSts
		self._AmtAndRateSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotSpcfdRate', type=RateType13Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAndAmtAndRateSts', type=RateTypeAndAmountAndStatus57, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtAndRateSts', type=AmountAndRateStatus1, min=0, max=1, mutex_group=1, array=False),
	))

