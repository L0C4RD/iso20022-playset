import base_types
import SupplementaryData1
import SecuritiesMarketReportHeader1
import SecuritiesReferenceDeltaStatusReport5Choice

class FinancialInstrumentReportingReferenceDataDeltaReportV03(base_types._BaseFieldType):

	__slots__ = ["_FinInstrm", "_SplmtryData", "_RptHdr"]
	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if type(value) != auto else self.make_default("FinInstrm")

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrm', type=SecuritiesReferenceDeltaStatusReport5Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=SecuritiesMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
	))

