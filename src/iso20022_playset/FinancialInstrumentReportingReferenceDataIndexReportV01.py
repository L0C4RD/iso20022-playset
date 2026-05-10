from . import base_types
import SecuritiesMarketReportHeader1
import SupplementaryData1
import SecuritiesIndexReport1

class FinancialInstrumentReportingReferenceDataIndexReportV01(base_types._BaseFieldType):

	__slots__ = ["_RptHdr", "_IndxData", "_SplmtryData"]
	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if type(value) != auto else self.make_default("RptHdr")

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = None

	@property
	def IndxData(self):
		return self._IndxData

	@IndxData.setter
	def IndxData(self, value):
		self._IndxData = value if type(value) != auto else self.make_default("IndxData")

	@IndxData.deleter
	def IndxData(self):
		del self._IndxData
		self._IndxData = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptHdr', type=SecuritiesMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxData', type=SecuritiesIndexReport1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

