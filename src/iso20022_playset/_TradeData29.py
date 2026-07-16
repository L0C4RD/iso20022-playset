# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DetailedReportStatistics5
from . import DetailedTransactionStatistics2Choice
from . import SupplementaryData1

class TradeData29(base_types._BaseFieldType):

	__slots__ = ["_RptSttstcs", "_SplmtryData", "_TxSttstcs"]
	@property
	def RptSttstcs(self):
		return self._RptSttstcs

	@RptSttstcs.setter
	def RptSttstcs(self, value):
		self._RptSttstcs = value if value is not None else base_types.UninitialisedField(self, 'RptSttstcs', DetailedReportStatistics5, True)

	@RptSttstcs.deleter
	def RptSttstcs(self):
		del self._RptSttstcs
		self._RptSttstcs = base_types.UninitialisedField(self, 'RptSttstcs', DetailedReportStatistics5, True)

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
	def TxSttstcs(self):
		return self._TxSttstcs

	@TxSttstcs.setter
	def TxSttstcs(self, value):
		self._TxSttstcs = value if value is not None else base_types.UninitialisedField(self, 'TxSttstcs', DetailedTransactionStatistics2Choice, True)

	@TxSttstcs.deleter
	def TxSttstcs(self):
		del self._TxSttstcs
		self._TxSttstcs = base_types.UninitialisedField(self, 'TxSttstcs', DetailedTransactionStatistics2Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptSttstcs', type=DetailedReportStatistics5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSttstcs', type=DetailedTransactionStatistics2Choice, min=1, max=None, mutex_group=None, array=True),
	))