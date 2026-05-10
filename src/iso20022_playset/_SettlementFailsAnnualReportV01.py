from . import base_types
from ._SettlementFailsData4 import SettlementFailsData4
from ._SettlementFailsReportHeader2 import SettlementFailsReportHeader2
from ._SupplementaryData1 import SupplementaryData1

class SettlementFailsAnnualReportV01(base_types._BaseFieldType):

	__slots__ = ["_AnlAggt", "_RptHdr", "_SplmtryData"]
	@property
	def AnlAggt(self):
		return self._AnlAggt

	@AnlAggt.setter
	def AnlAggt(self, value):
		self._AnlAggt = value if type(value) != base_types.auto else self.make_default("AnlAggt")

	@AnlAggt.deleter
	def AnlAggt(self):
		del self._AnlAggt
		self._AnlAggt = None

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
		base_types.FieldEntry(name='AnlAggt', type=SettlementFailsData4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptHdr', type=SettlementFailsReportHeader2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

