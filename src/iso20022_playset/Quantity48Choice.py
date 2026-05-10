from . import base_types
from .FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from .ProprietaryQuantity8 import ProprietaryQuantity8

class Quantity48Choice(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_PrtryQty"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def PrtryQty(self):
		return self._PrtryQty

	@PrtryQty.setter
	def PrtryQty(self, value):
		self._PrtryQty = value if type(value) != auto else self.make_default("PrtryQty")

	@PrtryQty.deleter
	def PrtryQty(self):
		del self._PrtryQty
		self._PrtryQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryQty', type=ProprietaryQuantity8, min=0, max=1, mutex_group=1, array=False),
	))

