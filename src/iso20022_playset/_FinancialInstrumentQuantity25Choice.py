from . import base_types
from ._DecimalNumber import DecimalNumber
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class FinancialInstrumentQuantity25Choice(base_types._BaseFieldType):

	__slots__ = ["_NmnlVal", "_MntryVal", "_Unit"]
	@property
	def MntryVal(self):
		return self._MntryVal

	@MntryVal.setter
	def MntryVal(self, value):
		self._MntryVal = value if type(value) != base_types.auto else self.make_default("MntryVal")

	@MntryVal.deleter
	def MntryVal(self):
		del self._MntryVal
		self._MntryVal = None

	@property
	def NmnlVal(self):
		return self._NmnlVal

	@NmnlVal.setter
	def NmnlVal(self, value):
		self._NmnlVal = value if type(value) != base_types.auto else self.make_default("NmnlVal")

	@NmnlVal.deleter
	def NmnlVal(self):
		del self._NmnlVal
		self._NmnlVal = None

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != base_types.auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MntryVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmnlVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

