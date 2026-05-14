# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._AmountAndRateStatus1 import AmountAndRateStatus1
from ._RateTypeAndAmountAndStatus57 import RateTypeAndAmountAndStatus57

class GrossDividendRateFormat37Choice(base_types._BaseFieldType):

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
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtAndRateSts', type=AmountAndRateStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAndAmtAndRateSts', type=RateTypeAndAmountAndStatus57, min=0, max=1, mutex_group=1, array=False),
	))