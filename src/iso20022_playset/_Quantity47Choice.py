from . import base_types
from .Max52Text import Max52Text
from .LongFraction19DecimalNumber import LongFraction19DecimalNumber

class Quantity47Choice(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_Desc"]
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
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Desc', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
	))

