import base_types
import DecimalNumber

class FinancialInstrumentQuantity1(base_types._BaseFieldType):

	__slots__ = ["_Unit"]
	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Unit', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

