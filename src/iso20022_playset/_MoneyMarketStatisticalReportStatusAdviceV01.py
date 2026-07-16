# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MoneyMarketStatusReportHeader1
from . import MoneyMarketTransactionStatus2
from . import SupplementaryData1

class MoneyMarketStatisticalReportStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_StsRptHdr", "_TxSts"]
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
	def StsRptHdr(self):
		return self._StsRptHdr

	@StsRptHdr.setter
	def StsRptHdr(self, value):
		self._StsRptHdr = value if value is not None else base_types.UninitialisedField(self, 'StsRptHdr', MoneyMarketStatusReportHeader1, False)

	@StsRptHdr.deleter
	def StsRptHdr(self):
		del self._StsRptHdr
		self._StsRptHdr = base_types.UninitialisedField(self, 'StsRptHdr', MoneyMarketStatusReportHeader1, False)

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', MoneyMarketTransactionStatus2, True)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', MoneyMarketTransactionStatus2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsRptHdr', type=MoneyMarketStatusReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=MoneyMarketTransactionStatus2, min=0, max=None, mutex_group=None, array=True),
	))