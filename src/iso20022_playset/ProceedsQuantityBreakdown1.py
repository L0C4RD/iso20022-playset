import base_types
import FinancialInstrumentQuantity18Choice

class ProceedsQuantityBreakdown1(base_types._BaseFieldType):

	__slots__ = ["_CshCompstnQty", "_TrfOfRcvdPrcdsQty"]
	@property
	def CshCompstnQty(self):
		return self._CshCompstnQty

	@CshCompstnQty.setter
	def CshCompstnQty(self, value):
		self._CshCompstnQty = value if type(value) != auto else self.make_default("CshCompstnQty")

	@CshCompstnQty.deleter
	def CshCompstnQty(self):
		del self._CshCompstnQty
		self._CshCompstnQty = None

	@property
	def TrfOfRcvdPrcdsQty(self):
		return self._TrfOfRcvdPrcdsQty

	@TrfOfRcvdPrcdsQty.setter
	def TrfOfRcvdPrcdsQty(self, value):
		self._TrfOfRcvdPrcdsQty = value if type(value) != auto else self.make_default("TrfOfRcvdPrcdsQty")

	@TrfOfRcvdPrcdsQty.deleter
	def TrfOfRcvdPrcdsQty(self):
		del self._TrfOfRcvdPrcdsQty
		self._TrfOfRcvdPrcdsQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshCompstnQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfOfRcvdPrcdsQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
	))

