# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ForeignExchangeTerms24

class AmountAndForeignExchange1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_FX"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if value is not None else base_types.UninitialisedField(self, 'FX', ForeignExchangeTerms24, False)

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = base_types.UninitialisedField(self, 'FX', ForeignExchangeTerms24, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FX', type=ForeignExchangeTerms24, min=0, max=1, mutex_group=None, array=False),
	))