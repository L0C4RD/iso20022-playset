# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import RestrictedFINActiveOrHistoricCurrencyAnd13DecimalAmount
from . import YesNoIndicator

class PriceRateOrAmountOrUnknown3Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Rate", "_UknwnInd"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', RestrictedFINActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', RestrictedFINActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@property
	def UknwnInd(self):
		return self._UknwnInd

	@UknwnInd.setter
	def UknwnInd(self, value):
		self._UknwnInd = value if value is not None else base_types.UninitialisedField(self, 'UknwnInd', YesNoIndicator, False)

	@UknwnInd.deleter
	def UknwnInd(self):
		del self._UknwnInd
		self._UknwnInd = base_types.UninitialisedField(self, 'UknwnInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UknwnInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))