# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesMarketReportHeader1
from . import SecuritiesReferenceDataReport7
from . import SupplementaryData1

class FinancialInstrumentReportingCancellationReportV01(base_types._BaseFieldType):

	__slots__ = ["_CxlData", "_RptHdr", "_SplmtryData"]
	@property
	def CxlData(self):
		return self._CxlData

	@CxlData.setter
	def CxlData(self, value):
		self._CxlData = value if value is not None else base_types.UninitialisedField(self, 'CxlData', SecuritiesReferenceDataReport7, True)

	@CxlData.deleter
	def CxlData(self):
		del self._CxlData
		self._CxlData = base_types.UninitialisedField(self, 'CxlData', SecuritiesReferenceDataReport7, True)

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if value is not None else base_types.UninitialisedField(self, 'RptHdr', SecuritiesMarketReportHeader1, False)

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = base_types.UninitialisedField(self, 'RptHdr', SecuritiesMarketReportHeader1, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlData', type=SecuritiesReferenceDataReport7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=SecuritiesMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))