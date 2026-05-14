# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvoiceTaxReportTransactionStatus1 import InvoiceTaxReportTransactionStatus1
from ._InvoiceTaxStatusReportHeader1 import InvoiceTaxStatusReportHeader1
from ._SupplementaryData1 import SupplementaryData1

class InvoiceTaxReportStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_StsRptHdr", "_TxSts"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def StsRptHdr(self):
		return self._StsRptHdr

	@StsRptHdr.setter
	def StsRptHdr(self, value):
		self._StsRptHdr = value if type(value) != base_types.auto else self.make_default("StsRptHdr")

	@StsRptHdr.deleter
	def StsRptHdr(self):
		del self._StsRptHdr
		self._StsRptHdr = None

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != base_types.auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsRptHdr', type=InvoiceTaxStatusReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=InvoiceTaxReportTransactionStatus1, min=0, max=None, mutex_group=None, array=True),
	))