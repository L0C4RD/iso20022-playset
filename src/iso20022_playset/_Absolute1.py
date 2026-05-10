from . import base_types
from ._Max35Text import Max35Text
from ._Number import Number

class Absolute1(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_Unit"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

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
		base_types.FieldEntry(name='Qty', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

