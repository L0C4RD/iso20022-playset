# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RateStatus1Code
from . import RestrictedFINActiveCurrencyAnd13DecimalAmount

class AmountAndRateStatus2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_RateSts"]
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
	def RateSts(self):
		return self._RateSts

	@RateSts.setter
	def RateSts(self, value):
		self._RateSts = value if value is not None else base_types.UninitialisedField(self, 'RateSts', RateStatus1Code, False)

	@RateSts.deleter
	def RateSts(self):
		del self._RateSts
		self._RateSts = base_types.UninitialisedField(self, 'RateSts', RateStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateSts', type=RateStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))