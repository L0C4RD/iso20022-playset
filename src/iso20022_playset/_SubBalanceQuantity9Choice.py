from . import base_types
from ._FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice
from ._QuantityAndAvailability4 import QuantityAndAvailability4
from ._GenericIdentification144 import GenericIdentification144

class SubBalanceQuantity9Choice(base_types._BaseFieldType):

	__slots__ = ["_QtyAndAvlbty", "_Qty", "_Prtry"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

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
	def QtyAndAvlbty(self):
		return self._QtyAndAvlbty

	@QtyAndAvlbty.setter
	def QtyAndAvlbty(self, value):
		self._QtyAndAvlbty = value if type(value) != base_types.auto else self.make_default("QtyAndAvlbty")

	@QtyAndAvlbty.deleter
	def QtyAndAvlbty(self):
		del self._QtyAndAvlbty
		self._QtyAndAvlbty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification144, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyAndAvlbty', type=QuantityAndAvailability4, min=0, max=1, mutex_group=1, array=False),
	))

