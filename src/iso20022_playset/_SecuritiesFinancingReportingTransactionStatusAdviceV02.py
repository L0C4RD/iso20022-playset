# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SupplementaryData1
from . import TradeData35Choice

class SecuritiesFinancingReportingTransactionStatusAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_TxRptStsAndRsn"]
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
	def TxRptStsAndRsn(self):
		return self._TxRptStsAndRsn

	@TxRptStsAndRsn.setter
	def TxRptStsAndRsn(self, value):
		self._TxRptStsAndRsn = value if value is not None else base_types.UninitialisedField(self, 'TxRptStsAndRsn', TradeData35Choice, True)

	@TxRptStsAndRsn.deleter
	def TxRptStsAndRsn(self):
		del self._TxRptStsAndRsn
		self._TxRptStsAndRsn = base_types.UninitialisedField(self, 'TxRptStsAndRsn', TradeData35Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxRptStsAndRsn', type=TradeData35Choice, min=1, max=None, mutex_group=None, array=True),
	))