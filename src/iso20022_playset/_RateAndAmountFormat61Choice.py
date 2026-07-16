# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import Percentage14Rate
from . import RateTypeAndAmountAndStatus37
from . import RateTypeAndPercentageRate14
from . import RateValueType7Code

class RateAndAmountFormat61Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_NotSpcfdRate", "_Rate", "_RateTpAndAmtAndRateSts", "_RateTpAndRate"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAnd13DecimalAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfdRate', RateValueType7Code, False)

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = base_types.UninitialisedField(self, 'NotSpcfdRate', RateValueType7Code, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', Percentage14Rate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', Percentage14Rate, False)

	@property
	def RateTpAndAmtAndRateSts(self):
		return self._RateTpAndAmtAndRateSts

	@RateTpAndAmtAndRateSts.setter
	def RateTpAndAmtAndRateSts(self, value):
		self._RateTpAndAmtAndRateSts = value if value is not None else base_types.UninitialisedField(self, 'RateTpAndAmtAndRateSts', RateTypeAndAmountAndStatus37, False)

	@RateTpAndAmtAndRateSts.deleter
	def RateTpAndAmtAndRateSts(self):
		del self._RateTpAndAmtAndRateSts
		self._RateTpAndAmtAndRateSts = base_types.UninitialisedField(self, 'RateTpAndAmtAndRateSts', RateTypeAndAmountAndStatus37, False)

	@property
	def RateTpAndRate(self):
		return self._RateTpAndRate

	@RateTpAndRate.setter
	def RateTpAndRate(self, value):
		self._RateTpAndRate = value if value is not None else base_types.UninitialisedField(self, 'RateTpAndRate', RateTypeAndPercentageRate14, False)

	@RateTpAndRate.deleter
	def RateTpAndRate(self):
		del self._RateTpAndRate
		self._RateTpAndRate = base_types.UninitialisedField(self, 'RateTpAndRate', RateTypeAndPercentageRate14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateValueType7Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAndAmtAndRateSts', type=RateTypeAndAmountAndStatus37, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAndRate', type=RateTypeAndPercentageRate14, min=0, max=1, mutex_group=1, array=False),
	))