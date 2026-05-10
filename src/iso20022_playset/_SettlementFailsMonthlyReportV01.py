from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._SettlementFailsData3 import SettlementFailsData3
from ._SettlementFailsReportHeader2 import SettlementFailsReportHeader2
from ._SettlementFailsDailyData3 import SettlementFailsDailyData3

class SettlementFailsMonthlyReportV01(base_types._BaseFieldType):

	__slots__ = ["_RptHdr", "_SplmtryData", "_DalyData", "_MnthlyAggt"]
	@property
	def DalyData(self):
		return self._DalyData

	@DalyData.setter
	def DalyData(self, value):
		self._DalyData = value if type(value) != base_types.auto else self.make_default("DalyData")

	@DalyData.deleter
	def DalyData(self):
		del self._DalyData
		self._DalyData = None

	@property
	def MnthlyAggt(self):
		return self._MnthlyAggt

	@MnthlyAggt.setter
	def MnthlyAggt(self, value):
		self._MnthlyAggt = value if type(value) != base_types.auto else self.make_default("MnthlyAggt")

	@MnthlyAggt.deleter
	def MnthlyAggt(self):
		del self._MnthlyAggt
		self._MnthlyAggt = None

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
		base_types.FieldEntry(name='DalyData', type=SettlementFailsDailyData3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MnthlyAggt', type=SettlementFailsData3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptHdr', type=SettlementFailsReportHeader2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

