from . import base_types
from ._SecuritiesMarketReportHeader1 import SecuritiesMarketReportHeader1
from ._SupplementaryData1 import SupplementaryData1
from ._VolumeCapResult1 import VolumeCapResult1

class FinancialInstrumentReportingTradingVolumeCapResultReportV01(base_types._BaseFieldType):

	__slots__ = ["_VolCapRslt", "_SplmtryData", "_RptHdr"]
	@property
	def VolCapRslt(self):
		return self._VolCapRslt

	@VolCapRslt.setter
	def VolCapRslt(self, value):
		self._VolCapRslt = value if type(value) != base_types.auto else self.make_default("VolCapRslt")

	@VolCapRslt.deleter
	def VolCapRslt(self):
		del self._VolCapRslt
		self._VolCapRslt = None

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
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if type(value) != base_types.auto else self.make_default("RptHdr")

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VolCapRslt', type=VolumeCapResult1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=SecuritiesMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
	))

