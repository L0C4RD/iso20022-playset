from . import base_types
from ._FinancialInstrumentQuantityChoice import FinancialInstrumentQuantityChoice
from ._GenericIdentification6 import GenericIdentification6
from ._QuantityAndAvailability import QuantityAndAvailability

class SubBalanceQuantity1Choice(base_types._BaseFieldType):

	__slots__ = ["_QtyAsDSS", "_QtyAndAvlbty", "_Qty"]
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

	@property
	def QtyAsDSS(self):
		return self._QtyAsDSS

	@QtyAsDSS.setter
	def QtyAsDSS(self, value):
		self._QtyAsDSS = value if type(value) != base_types.auto else self.make_default("QtyAsDSS")

	@QtyAsDSS.deleter
	def QtyAsDSS(self):
		del self._QtyAsDSS
		self._QtyAsDSS = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantityChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyAndAvlbty', type=QuantityAndAvailability, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyAsDSS', type=GenericIdentification6, min=0, max=1, mutex_group=1, array=False),
	))

