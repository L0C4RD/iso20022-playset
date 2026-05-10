from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._DecimalNumber import DecimalNumber

class UnitsOrAmount1Choice(base_types._BaseFieldType):

	__slots__ = ["_Unit", "_Amt"]
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
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

