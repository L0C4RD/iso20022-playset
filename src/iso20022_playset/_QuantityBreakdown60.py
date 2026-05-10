from . import base_types
from ._GenericIdentification37 import GenericIdentification37
from ._FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice

class QuantityBreakdown60(base_types._BaseFieldType):

	__slots__ = ["_LotQty", "_LotNb"]
	@property
	def LotNb(self):
		return self._LotNb

	@LotNb.setter
	def LotNb(self, value):
		self._LotNb = value if type(value) != base_types.auto else self.make_default("LotNb")

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = None

	@property
	def LotQty(self):
		return self._LotQty

	@LotQty.setter
	def LotQty(self, value):
		self._LotQty = value if type(value) != base_types.auto else self.make_default("LotQty")

	@LotQty.deleter
	def LotQty(self):
		del self._LotQty
		self._LotQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotNb', type=GenericIdentification37, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
	))

