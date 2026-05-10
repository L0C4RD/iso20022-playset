from . import base_types
from ._Balance23 import Balance23
from ._Price3 import Price3
from ._TypeOfPrice32Choice import TypeOfPrice32Choice
from ._BalanceAmounts6 import BalanceAmounts6
from ._GenericIdentification39 import GenericIdentification39
from ._DateAndDateTime2Choice import DateAndDateTime2Choice

class QuantityBreakdown70(base_types._BaseFieldType):

	__slots__ = ["_AcctBaseCcyAmts", "_LotNb", "_LotQty", "_AltrnRptgCcyAmts", "_TpOfPric", "_LotPric", "_LotDtTm", "_InstrmCcyAmts"]
	@property
	def AcctBaseCcyAmts(self):
		return self._AcctBaseCcyAmts

	@AcctBaseCcyAmts.setter
	def AcctBaseCcyAmts(self, value):
		self._AcctBaseCcyAmts = value if type(value) != base_types.auto else self.make_default("AcctBaseCcyAmts")

	@AcctBaseCcyAmts.deleter
	def AcctBaseCcyAmts(self):
		del self._AcctBaseCcyAmts
		self._AcctBaseCcyAmts = None

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

	@property
	def AltrnRptgCcyAmts(self):
		return self._AltrnRptgCcyAmts

	@AltrnRptgCcyAmts.setter
	def AltrnRptgCcyAmts(self, value):
		self._AltrnRptgCcyAmts = value if type(value) != base_types.auto else self.make_default("AltrnRptgCcyAmts")

	@AltrnRptgCcyAmts.deleter
	def AltrnRptgCcyAmts(self):
		del self._AltrnRptgCcyAmts
		self._AltrnRptgCcyAmts = None

	@property
	def TpOfPric(self):
		return self._TpOfPric

	@TpOfPric.setter
	def TpOfPric(self, value):
		self._TpOfPric = value if type(value) != base_types.auto else self.make_default("TpOfPric")

	@TpOfPric.deleter
	def TpOfPric(self):
		del self._TpOfPric
		self._TpOfPric = None

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
	def InstrmCcyAmts(self):
		return self._InstrmCcyAmts

	@InstrmCcyAmts.setter
	def InstrmCcyAmts(self, value):
		self._InstrmCcyAmts = value if type(value) != base_types.auto else self.make_default("InstrmCcyAmts")

	@InstrmCcyAmts.deleter
	def InstrmCcyAmts(self):
		del self._InstrmCcyAmts
		self._InstrmCcyAmts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyAmts', type=BalanceAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotNb', type=GenericIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=Balance23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnRptgCcyAmts', type=BalanceAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfPric', type=TypeOfPrice32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotPric', type=Price3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmCcyAmts', type=BalanceAmounts6, min=0, max=1, mutex_group=None, array=False),
	))

