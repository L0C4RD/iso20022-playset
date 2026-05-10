from . import base_types
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .Price7 import Price7
from .GenericIdentification37 import GenericIdentification37
from .FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from .TypeOfPrice29Choice import TypeOfPrice29Choice

class QuantityBreakdown62(base_types._BaseFieldType):

	__slots__ = ["_LotQty", "_TpOfPric", "_LotDtTm", "_LotNb", "_LotPric"]
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
	def TpOfPric(self):
		return self._TpOfPric

	@TpOfPric.setter
	def TpOfPric(self, value):
		self._TpOfPric = value if type(value) != auto else self.make_default("TpOfPric")

	@TpOfPric.deleter
	def TpOfPric(self):
		del self._TpOfPric
		self._TpOfPric = None

	@property
	def LotDtTm(self):
		return self._LotDtTm

	@LotDtTm.setter
	def LotDtTm(self, value):
		self._LotDtTm = value if type(value) != auto else self.make_default("LotDtTm")

	@LotDtTm.deleter
	def LotDtTm(self):
		del self._LotDtTm
		self._LotDtTm = None

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
	def LotPric(self):
		return self._LotPric

	@LotPric.setter
	def LotPric(self, value):
		self._LotPric = value if type(value) != auto else self.make_default("LotPric")

	@LotPric.deleter
	def LotPric(self):
		del self._LotPric
		self._LotPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfPric', type=TypeOfPrice29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotNb', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotPric', type=Price7, min=0, max=1, mutex_group=None, array=False),
	))

