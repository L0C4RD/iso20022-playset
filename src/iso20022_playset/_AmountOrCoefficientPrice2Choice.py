# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import DecimalNumber
from . import ImpliedCurrencyAndAmount

class AmountOrCoefficientPrice2Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtWthCcy", "_Coeff"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def AmtWthCcy(self):
		return self._AmtWthCcy

	@AmtWthCcy.setter
	def AmtWthCcy(self, value):
		self._AmtWthCcy = value if value is not None else base_types.UninitialisedField(self, 'AmtWthCcy', ActiveOrHistoricCurrencyAndAmount, False)

	@AmtWthCcy.deleter
	def AmtWthCcy(self):
		del self._AmtWthCcy
		self._AmtWthCcy = base_types.UninitialisedField(self, 'AmtWthCcy', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def Coeff(self):
		return self._Coeff

	@Coeff.setter
	def Coeff(self, value):
		self._Coeff = value if value is not None else base_types.UninitialisedField(self, 'Coeff', DecimalNumber, False)

	@Coeff.deleter
	def Coeff(self):
		del self._Coeff
		self._Coeff = base_types.UninitialisedField(self, 'Coeff', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtWthCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Coeff', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))