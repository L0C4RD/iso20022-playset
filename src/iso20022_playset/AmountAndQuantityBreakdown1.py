import base_types
import GenericIdentification37
import AmountAndDirection5
import FinancialInstrumentQuantity1Choice
import GenericIdentification30

class AmountAndQuantityBreakdown1(base_types._BaseFieldType):

	__slots__ = ["_LotNb", "_LotAmt", "_LotQty", "_CshSubBalTp"]
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

	@property
	def LotAmt(self):
		return self._LotAmt

	@LotAmt.setter
	def LotAmt(self, value):
		self._LotAmt = value if type(value) != auto else self.make_default("LotAmt")

	@LotAmt.deleter
	def LotAmt(self):
		del self._LotAmt
		self._LotAmt = None

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
	def CshSubBalTp(self):
		return self._CshSubBalTp

	@CshSubBalTp.setter
	def CshSubBalTp(self, value):
		self._CshSubBalTp = value if type(value) != auto else self.make_default("CshSubBalTp")

	@CshSubBalTp.deleter
	def CshSubBalTp(self):
		del self._CshSubBalTp
		self._CshSubBalTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotNb', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSubBalTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
	))

