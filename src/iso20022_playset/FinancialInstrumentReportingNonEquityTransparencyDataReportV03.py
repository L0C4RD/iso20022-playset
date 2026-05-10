from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .SecuritiesMarketReportHeader1 import SecuritiesMarketReportHeader1
from .TransparencyDataReport21 import TransparencyDataReport21

class FinancialInstrumentReportingNonEquityTransparencyDataReportV03(base_types._BaseFieldType):

	__slots__ = ["_NonEqtyTrnsprncyData", "_SplmtryData", "_RptHdr"]
	@property
	def NonEqtyTrnsprncyData(self):
		return self._NonEqtyTrnsprncyData

	@NonEqtyTrnsprncyData.setter
	def NonEqtyTrnsprncyData(self, value):
		self._NonEqtyTrnsprncyData = value if type(value) != auto else self.make_default("NonEqtyTrnsprncyData")

	@NonEqtyTrnsprncyData.deleter
	def NonEqtyTrnsprncyData(self):
		del self._NonEqtyTrnsprncyData
		self._NonEqtyTrnsprncyData = None

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
		base_types.FieldEntry(name='NonEqtyTrnsprncyData', type=TransparencyDataReport21, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=SecuritiesMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
	))

