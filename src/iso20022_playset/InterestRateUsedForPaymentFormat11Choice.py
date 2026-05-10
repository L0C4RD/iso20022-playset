from . import base_types
import ActiveCurrencyAnd13DecimalAmount
import Percentage14Rate
import RateTypeAndAmountAndStatus24
import RateType13Code

class InterestRateUsedForPaymentFormat11Choice(base_types._BaseFieldType):

	__slots__ = ["_RateTpAndAmtAndRateSts", "_Rate", "_Amt", "_NotSpcfdRate"]
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
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

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
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if type(value) != auto else self.make_default("NotSpcfdRate")

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateTpAndAmtAndRateSts', type=RateTypeAndAmountAndStatus24, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateType13Code, min=0, max=1, mutex_group=1, array=False),
	))

