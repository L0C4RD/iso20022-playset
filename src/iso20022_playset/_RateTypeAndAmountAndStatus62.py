# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RateStatus4Choice
from . import RateType83Choice
from . import RestrictedFINActiveCurrencyAnd13DecimalAmount

class RateTypeAndAmountAndStatus62(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_RateSts", "_RateTp"]
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
		self._RateSts = value if value is not None else base_types.UninitialisedField(self, 'RateSts', RateStatus4Choice, False)

	@RateSts.deleter
	def RateSts(self):
		del self._RateSts
		self._RateSts = base_types.UninitialisedField(self, 'RateSts', RateStatus4Choice, False)

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if value is not None else base_types.UninitialisedField(self, 'RateTp', RateType83Choice, False)

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = base_types.UninitialisedField(self, 'RateTp', RateType83Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateSts', type=RateStatus4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType83Choice, min=1, max=1, mutex_group=None, array=False),
	))