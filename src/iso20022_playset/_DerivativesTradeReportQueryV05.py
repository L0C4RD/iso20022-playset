# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification121Choice
from . import SupplementaryData1
from . import TradeReportQuery18Choice

class DerivativesTradeReportQueryV05(base_types._BaseFieldType):

	__slots__ = ["_RqstngAuthrty", "_SplmtryData", "_TradQryData"]
	@property
	def RqstngAuthrty(self):
		return self._RqstngAuthrty

	@RqstngAuthrty.setter
	def RqstngAuthrty(self, value):
		self._RqstngAuthrty = value if value is not None else base_types.UninitialisedField(self, 'RqstngAuthrty', PartyIdentification121Choice, False)

	@RqstngAuthrty.deleter
	def RqstngAuthrty(self):
		del self._RqstngAuthrty
		self._RqstngAuthrty = base_types.UninitialisedField(self, 'RqstngAuthrty', PartyIdentification121Choice, False)

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
	def TradQryData(self):
		return self._TradQryData

	@TradQryData.setter
	def TradQryData(self, value):
		self._TradQryData = value if value is not None else base_types.UninitialisedField(self, 'TradQryData', TradeReportQuery18Choice, False)

	@TradQryData.deleter
	def TradQryData(self):
		del self._TradQryData
		self._TradQryData = base_types.UninitialisedField(self, 'TradQryData', TradeReportQuery18Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RqstngAuthrty', type=PartyIdentification121Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradQryData', type=TradeReportQuery18Choice, min=1, max=1, mutex_group=None, array=False),
	))