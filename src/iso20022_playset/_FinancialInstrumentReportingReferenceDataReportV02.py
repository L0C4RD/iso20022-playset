# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesMarketReportHeader1 import SecuritiesMarketReportHeader1
from ._SecuritiesReferenceDataReport6 import SecuritiesReferenceDataReport6
from ._SupplementaryData1 import SupplementaryData1

class FinancialInstrumentReportingReferenceDataReportV02(base_types._BaseFieldType):

	__slots__ = ["_RefData", "_RptHdr", "_SplmtryData"]
	@property
	def RefData(self):
		return self._RefData

	@RefData.setter
	def RefData(self, value):
		self._RefData = value if type(value) != base_types.auto else self.make_default("RefData")

	@RefData.deleter
	def RefData(self):
		del self._RefData
		self._RefData = None

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if type(value) != base_types.auto else self.make_default("RptHdr")

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefData', type=SecuritiesReferenceDataReport6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=SecuritiesMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))