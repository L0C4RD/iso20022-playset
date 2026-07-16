# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount

class AmountToAmountRatio2(base_types._BaseFieldType):

	__slots__ = ["_Amt1", "_Amt2"]
	@property
	def Amt1(self):
		return self._Amt1

	@Amt1.setter
	def Amt1(self, value):
		self._Amt1 = value if value is not None else base_types.UninitialisedField(self, 'Amt1', ActiveCurrencyAnd13DecimalAmount, False)

	@Amt1.deleter
	def Amt1(self):
		del self._Amt1
		self._Amt1 = base_types.UninitialisedField(self, 'Amt1', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def Amt2(self):
		return self._Amt2

	@Amt2.setter
	def Amt2(self, value):
		self._Amt2 = value if value is not None else base_types.UninitialisedField(self, 'Amt2', ActiveCurrencyAnd13DecimalAmount, False)

	@Amt2.deleter
	def Amt2(self):
		del self._Amt2
		self._Amt2 = base_types.UninitialisedField(self, 'Amt2', ActiveCurrencyAnd13DecimalAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt1', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt2', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
	))