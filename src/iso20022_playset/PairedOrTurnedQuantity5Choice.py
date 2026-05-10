from . import base_types
import FinancialInstrumentQuantity33Choice

class PairedOrTurnedQuantity5Choice(base_types._BaseFieldType):

	__slots__ = ["_PairdOffQty", "_TrndQty"]
	@property
	def PairdOffQty(self):
		return self._PairdOffQty

	@PairdOffQty.setter
	def PairdOffQty(self, value):
		self._PairdOffQty = value if type(value) != auto else self.make_default("PairdOffQty")

	@PairdOffQty.deleter
	def PairdOffQty(self):
		del self._PairdOffQty
		self._PairdOffQty = None

	@property
	def TrndQty(self):
		return self._TrndQty

	@TrndQty.setter
	def TrndQty(self, value):
		self._TrndQty = value if type(value) != auto else self.make_default("TrndQty")

	@TrndQty.deleter
	def TrndQty(self):
		del self._TrndQty
		self._TrndQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PairdOffQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrndQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=1, array=False),
	))

