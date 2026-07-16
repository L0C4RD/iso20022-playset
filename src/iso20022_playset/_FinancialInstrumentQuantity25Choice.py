# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import DecimalNumber

class FinancialInstrumentQuantity25Choice(base_types._BaseFieldType):

	__slots__ = ["_MntryVal", "_NmnlVal", "_Unit"]
	@property
	def MntryVal(self):
		return self._MntryVal

	@MntryVal.setter
	def MntryVal(self, value):
		self._MntryVal = value if value is not None else base_types.UninitialisedField(self, 'MntryVal', ActiveOrHistoricCurrencyAndAmount, False)

	@MntryVal.deleter
	def MntryVal(self):
		del self._MntryVal
		self._MntryVal = base_types.UninitialisedField(self, 'MntryVal', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def NmnlVal(self):
		return self._NmnlVal

	@NmnlVal.setter
	def NmnlVal(self, value):
		self._NmnlVal = value if value is not None else base_types.UninitialisedField(self, 'NmnlVal', ActiveOrHistoricCurrencyAndAmount, False)

	@NmnlVal.deleter
	def NmnlVal(self):
		del self._NmnlVal
		self._NmnlVal = base_types.UninitialisedField(self, 'NmnlVal', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', DecimalNumber, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MntryVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmnlVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))