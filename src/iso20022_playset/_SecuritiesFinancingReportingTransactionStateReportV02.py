# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SupplementaryData1
from . import TradeStateReport5Choice

class SecuritiesFinancingReportingTransactionStateReportV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_TradData"]
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
	def TradData(self):
		return self._TradData

	@TradData.setter
	def TradData(self, value):
		self._TradData = value if value is not None else base_types.UninitialisedField(self, 'TradData', TradeStateReport5Choice, False)

	@TradData.deleter
	def TradData(self):
		del self._TradData
		self._TradData = base_types.UninitialisedField(self, 'TradData', TradeStateReport5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradData', type=TradeStateReport5Choice, min=1, max=1, mutex_group=None, array=False),
	))