from . import base_types
from .AmountAndDirection53 import AmountAndDirection53
from .DecimalNumber import DecimalNumber

class QuantityNominalValue2Choice(base_types._BaseFieldType):

	__slots__ = ["_NmnlVal", "_Qty"]
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
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NmnlVal', type=AmountAndDirection53, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

