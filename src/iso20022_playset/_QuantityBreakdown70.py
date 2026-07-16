# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Balance23
from . import BalanceAmounts6
from . import DateAndDateTime2Choice
from . import GenericIdentification39
from . import Price3
from . import TypeOfPrice32Choice

class QuantityBreakdown70(base_types._BaseFieldType):

	__slots__ = ["_AcctBaseCcyAmts", "_AltrnRptgCcyAmts", "_InstrmCcyAmts", "_LotDtTm", "_LotNb", "_LotPric", "_LotQty", "_TpOfPric"]
	@property
	def AcctBaseCcyAmts(self):
		return self._AcctBaseCcyAmts

	@AcctBaseCcyAmts.setter
	def AcctBaseCcyAmts(self, value):
		self._AcctBaseCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts6, False)

	@AcctBaseCcyAmts.deleter
	def AcctBaseCcyAmts(self):
		del self._AcctBaseCcyAmts
		self._AcctBaseCcyAmts = base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts6, False)

	@property
	def AltrnRptgCcyAmts(self):
		return self._AltrnRptgCcyAmts

	@AltrnRptgCcyAmts.setter
	def AltrnRptgCcyAmts(self, value):
		self._AltrnRptgCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'AltrnRptgCcyAmts', BalanceAmounts6, False)

	@AltrnRptgCcyAmts.deleter
	def AltrnRptgCcyAmts(self):
		del self._AltrnRptgCcyAmts
		self._AltrnRptgCcyAmts = base_types.UninitialisedField(self, 'AltrnRptgCcyAmts', BalanceAmounts6, False)

	@property
	def InstrmCcyAmts(self):
		return self._InstrmCcyAmts

	@InstrmCcyAmts.setter
	def InstrmCcyAmts(self, value):
		self._InstrmCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts6, False)

	@InstrmCcyAmts.deleter
	def InstrmCcyAmts(self):
		del self._InstrmCcyAmts
		self._InstrmCcyAmts = base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts6, False)

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
		self._LotNb = value if value is not None else base_types.UninitialisedField(self, 'LotNb', GenericIdentification39, False)

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = base_types.UninitialisedField(self, 'LotNb', GenericIdentification39, False)

	@property
	def LotPric(self):
		return self._LotPric

	@LotPric.setter
	def LotPric(self, value):
		self._LotPric = value if value is not None else base_types.UninitialisedField(self, 'LotPric', Price3, False)

	@LotPric.deleter
	def LotPric(self):
		del self._LotPric
		self._LotPric = base_types.UninitialisedField(self, 'LotPric', Price3, False)

	@property
	def LotQty(self):
		return self._LotQty

	@LotQty.setter
	def LotQty(self, value):
		self._LotQty = value if value is not None else base_types.UninitialisedField(self, 'LotQty', Balance23, False)

	@LotQty.deleter
	def LotQty(self):
		del self._LotQty
		self._LotQty = base_types.UninitialisedField(self, 'LotQty', Balance23, False)

	@property
	def TpOfPric(self):
		return self._TpOfPric

	@TpOfPric.setter
	def TpOfPric(self, value):
		self._TpOfPric = value if value is not None else base_types.UninitialisedField(self, 'TpOfPric', TypeOfPrice32Choice, False)

	@TpOfPric.deleter
	def TpOfPric(self):
		del self._TpOfPric
		self._TpOfPric = base_types.UninitialisedField(self, 'TpOfPric', TypeOfPrice32Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyAmts', type=BalanceAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnRptgCcyAmts', type=BalanceAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmCcyAmts', type=BalanceAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotNb', type=GenericIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotPric', type=Price3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=Balance23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfPric', type=TypeOfPrice32Choice, min=0, max=1, mutex_group=None, array=False),
	))