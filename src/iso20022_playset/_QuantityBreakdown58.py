# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Balance16
from . import BalanceAmounts2
from . import DateAndDateTime2Choice
from . import GenericIdentification37
from . import Price7
from . import TypeOfPrice29Choice

class QuantityBreakdown58(base_types._BaseFieldType):

	__slots__ = ["_AcctBaseCcyAmts", "_AltrnRptgCcyAmts", "_InstrmCcyAmts", "_LotDtTm", "_LotNb", "_LotPric", "_LotQty", "_TpOfPric"]
	@property
	def AcctBaseCcyAmts(self):
		return self._AcctBaseCcyAmts

	@AcctBaseCcyAmts.setter
	def AcctBaseCcyAmts(self, value):
		self._AcctBaseCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts2, False)

	@AcctBaseCcyAmts.deleter
	def AcctBaseCcyAmts(self):
		del self._AcctBaseCcyAmts
		self._AcctBaseCcyAmts = base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts2, False)

	@property
	def AltrnRptgCcyAmts(self):
		return self._AltrnRptgCcyAmts

	@AltrnRptgCcyAmts.setter
	def AltrnRptgCcyAmts(self, value):
		self._AltrnRptgCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'AltrnRptgCcyAmts', BalanceAmounts2, False)

	@AltrnRptgCcyAmts.deleter
	def AltrnRptgCcyAmts(self):
		del self._AltrnRptgCcyAmts
		self._AltrnRptgCcyAmts = base_types.UninitialisedField(self, 'AltrnRptgCcyAmts', BalanceAmounts2, False)

	@property
	def InstrmCcyAmts(self):
		return self._InstrmCcyAmts

	@InstrmCcyAmts.setter
	def InstrmCcyAmts(self, value):
		self._InstrmCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts2, False)

	@InstrmCcyAmts.deleter
	def InstrmCcyAmts(self):
		del self._InstrmCcyAmts
		self._InstrmCcyAmts = base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts2, False)

	@property
	def LotDtTm(self):
		return self._LotDtTm

	@LotDtTm.setter
	def LotDtTm(self, value):
		self._LotDtTm = value if value is not None else base_types.UninitialisedField(self, 'LotDtTm', DateAndDateTime2Choice, False)

	@LotDtTm.deleter
	def LotDtTm(self):
		del self._LotDtTm
		self._LotDtTm = base_types.UninitialisedField(self, 'LotDtTm', DateAndDateTime2Choice, False)

	@property
	def LotNb(self):
		return self._LotNb

	@LotNb.setter
	def LotNb(self, value):
		self._LotNb = value if value is not None else base_types.UninitialisedField(self, 'LotNb', GenericIdentification37, False)

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = base_types.UninitialisedField(self, 'LotNb', GenericIdentification37, False)

	@property
	def LotPric(self):
		return self._LotPric

	@LotPric.setter
	def LotPric(self, value):
		self._LotPric = value if value is not None else base_types.UninitialisedField(self, 'LotPric', Price7, False)

	@LotPric.deleter
	def LotPric(self):
		del self._LotPric
		self._LotPric = base_types.UninitialisedField(self, 'LotPric', Price7, False)

	@property
	def LotQty(self):
		return self._LotQty

	@LotQty.setter
	def LotQty(self, value):
		self._LotQty = value if value is not None else base_types.UninitialisedField(self, 'LotQty', Balance16, False)

	@LotQty.deleter
	def LotQty(self):
		del self._LotQty
		self._LotQty = base_types.UninitialisedField(self, 'LotQty', Balance16, False)

	@property
	def TpOfPric(self):
		return self._TpOfPric

	@TpOfPric.setter
	def TpOfPric(self, value):
		self._TpOfPric = value if value is not None else base_types.UninitialisedField(self, 'TpOfPric', TypeOfPrice29Choice, False)

	@TpOfPric.deleter
	def TpOfPric(self):
		del self._TpOfPric
		self._TpOfPric = base_types.UninitialisedField(self, 'TpOfPric', TypeOfPrice29Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyAmts', type=BalanceAmounts2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnRptgCcyAmts', type=BalanceAmounts2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmCcyAmts', type=BalanceAmounts2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotNb', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotPric', type=Price7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=Balance16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfPric', type=TypeOfPrice29Choice, min=0, max=1, mutex_group=None, array=False),
	))