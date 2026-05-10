from . import base_types
from ._GenericIdentification37 import GenericIdentification37
from ._DateAndDateTime1Choice import DateAndDateTime1Choice
from ._Price14 import Price14
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice

class QuantityBreakdown76(base_types._BaseFieldType):

	__slots__ = ["_LotNb", "_LotDtTm", "_LotQty", "_LotPric"]
	@property
	def LotDtTm(self):
		return self._LotDtTm

	@LotDtTm.setter
	def LotDtTm(self, value):
		self._LotDtTm = value if type(value) != base_types.auto else self.make_default("LotDtTm")

	@LotDtTm.deleter
	def LotDtTm(self):
		del self._LotDtTm
		self._LotDtTm = None

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
	def LotPric(self):
		return self._LotPric

	@LotPric.setter
	def LotPric(self, value):
		self._LotPric = value if type(value) != base_types.auto else self.make_default("LotPric")

	@LotPric.deleter
	def LotPric(self):
		del self._LotPric
		self._LotPric = None

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
		base_types.FieldEntry(name='LotDtTm', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotNb', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
	))

