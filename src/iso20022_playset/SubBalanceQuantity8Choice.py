import base_types
import QuantityAndAvailability3
import FinancialInstrumentQuantity33Choice
import GenericIdentification56

class SubBalanceQuantity8Choice(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_QtyAndAvlbty", "_Prtry"]
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
	def QtyAndAvlbty(self):
		return self._QtyAndAvlbty

	@QtyAndAvlbty.setter
	def QtyAndAvlbty(self, value):
		self._QtyAndAvlbty = value if type(value) != auto else self.make_default("QtyAndAvlbty")

	@QtyAndAvlbty.deleter
	def QtyAndAvlbty(self):
		del self._QtyAndAvlbty
		self._QtyAndAvlbty = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyAndAvlbty', type=QuantityAndAvailability3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification56, min=0, max=1, mutex_group=1, array=False),
	))

