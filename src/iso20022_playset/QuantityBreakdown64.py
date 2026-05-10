from . import base_types
import GenericIdentification39
import FinancialInstrumentQuantity36Choice

class QuantityBreakdown64(base_types._BaseFieldType):

	__slots__ = ["_LotQty", "_LotNb"]
	@property
	def LotQty(self):
		return self._LotQty

	@LotQty.setter
	def LotQty(self, value):
		self._LotQty = value if type(value) != auto else self.make_default("LotQty")

	@LotQty.deleter
	def LotQty(self):
		del self._LotQty
		self._LotQty = None

	@property
	def LotNb(self):
		return self._LotNb

	@LotNb.setter
	def LotNb(self, value):
		self._LotNb = value if type(value) != auto else self.make_default("LotNb")

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotNb', type=GenericIdentification39, min=1, max=1, mutex_group=None, array=False),
	))

