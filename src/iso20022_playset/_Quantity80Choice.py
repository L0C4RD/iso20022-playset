from . import base_types
from .ProprietaryQuantity10 import ProprietaryQuantity10
from .Quantity57Choice import Quantity57Choice

class Quantity80Choice(base_types._BaseFieldType):

	__slots__ = ["_QtyChc", "_PrtryQty"]
	@property
	def QtyChc(self):
		return self._QtyChc

	@QtyChc.setter
	def QtyChc(self, value):
		self._QtyChc = value if type(value) != base_types.auto else self.make_default("QtyChc")

	@QtyChc.deleter
	def QtyChc(self):
		del self._QtyChc
		self._QtyChc = None

	@property
	def PrtryQty(self):
		return self._PrtryQty

	@PrtryQty.setter
	def PrtryQty(self, value):
		self._PrtryQty = value if type(value) != base_types.auto else self.make_default("PrtryQty")

	@PrtryQty.deleter
	def PrtryQty(self):
		del self._PrtryQty
		self._PrtryQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyChc', type=Quantity57Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryQty', type=ProprietaryQuantity10, min=0, max=1, mutex_group=1, array=False),
	))

