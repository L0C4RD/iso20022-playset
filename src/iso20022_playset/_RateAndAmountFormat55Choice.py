# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import Percentage14Rate
from . import RateTypeAndPercentageRate12

class RateAndAmountFormat55Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Rate", "_RateTpAndRate"]
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
	def RateTpAndRate(self):
		return self._RateTpAndRate

	@RateTpAndRate.setter
	def RateTpAndRate(self, value):
		self._RateTpAndRate = value if value is not None else base_types.UninitialisedField(self, 'RateTpAndRate', RateTypeAndPercentageRate12, False)

	@RateTpAndRate.deleter
	def RateTpAndRate(self):
		del self._RateTpAndRate
		self._RateTpAndRate = base_types.UninitialisedField(self, 'RateTpAndRate', RateTypeAndPercentageRate12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAndRate', type=RateTypeAndPercentageRate12, min=0, max=1, mutex_group=1, array=False),
	))