# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Pagination1
from . import SupplementaryData1
from . import TradeData45
from . import TradeDataReport2

class ForeignExchangeTradeBulkStatusNotificationV06(base_types._BaseFieldType):

	__slots__ = ["_MsgPgntn", "_SplmtryData", "_StsDtls", "_TradDataRpt"]
	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if value is not None else base_types.UninitialisedField(self, 'MsgPgntn', Pagination1, False)

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = base_types.UninitialisedField(self, 'MsgPgntn', Pagination1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def StsDtls(self):
		return self._StsDtls

	@StsDtls.setter
	def StsDtls(self, value):
		self._StsDtls = value if value is not None else base_types.UninitialisedField(self, 'StsDtls', TradeData45, False)

	@StsDtls.deleter
	def StsDtls(self):
		del self._StsDtls
		self._StsDtls = base_types.UninitialisedField(self, 'StsDtls', TradeData45, False)

	@property
	def TradDataRpt(self):
		return self._TradDataRpt

	@TradDataRpt.setter
	def TradDataRpt(self, value):
		self._TradDataRpt = value if value is not None else base_types.UninitialisedField(self, 'TradDataRpt', TradeDataReport2, True)

	@TradDataRpt.deleter
	def TradDataRpt(self):
		del self._TradDataRpt
		self._TradDataRpt = base_types.UninitialisedField(self, 'TradDataRpt', TradeDataReport2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsDtls', type=TradeData45, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDataRpt', type=TradeDataReport2, min=1, max=None, mutex_group=None, array=True),
	))