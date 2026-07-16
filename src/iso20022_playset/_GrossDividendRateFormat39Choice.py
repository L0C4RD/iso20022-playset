# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndRateStatus2
from . import RateTypeAndAmountAndStatus59
from . import RestrictedFINActiveCurrencyAnd13DecimalAmount

class GrossDividendRateFormat39Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtAndRateSts", "_RateTpAndAmtAndRateSts"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', RestrictedFINActiveCurrencyAnd13DecimalAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', RestrictedFINActiveCurrencyAnd13DecimalAmount, False)

	@property
	def AmtAndRateSts(self):
		return self._AmtAndRateSts

	@AmtAndRateSts.setter
	def AmtAndRateSts(self, value):
		self._AmtAndRateSts = value if value is not None else base_types.UninitialisedField(self, 'AmtAndRateSts', AmountAndRateStatus2, False)

	@AmtAndRateSts.deleter
	def AmtAndRateSts(self):
		del self._AmtAndRateSts
		self._AmtAndRateSts = base_types.UninitialisedField(self, 'AmtAndRateSts', AmountAndRateStatus2, False)

	@property
	def RateTpAndAmtAndRateSts(self):
		return self._RateTpAndAmtAndRateSts

	@RateTpAndAmtAndRateSts.setter
	def RateTpAndAmtAndRateSts(self, value):
		self._RateTpAndAmtAndRateSts = value if value is not None else base_types.UninitialisedField(self, 'RateTpAndAmtAndRateSts', RateTypeAndAmountAndStatus59, False)

	@RateTpAndAmtAndRateSts.deleter
	def RateTpAndAmtAndRateSts(self):
		del self._RateTpAndAmtAndRateSts
		self._RateTpAndAmtAndRateSts = base_types.UninitialisedField(self, 'RateTpAndAmtAndRateSts', RateTypeAndAmountAndStatus59, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtAndRateSts', type=AmountAndRateStatus2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAndAmtAndRateSts', type=RateTypeAndAmountAndStatus59, min=0, max=1, mutex_group=1, array=False),
	))