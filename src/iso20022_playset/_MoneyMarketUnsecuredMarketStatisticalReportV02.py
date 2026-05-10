from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .MoneyMarketReportHeader1 import MoneyMarketReportHeader1
from .UnsecuredMarketReport4Choice import UnsecuredMarketReport4Choice

class MoneyMarketUnsecuredMarketStatisticalReportV02(base_types._BaseFieldType):

	__slots__ = ["_RptHdr", "_SplmtryData", "_UscrdMktRpt"]
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

	@property
	def UscrdMktRpt(self):
		return self._UscrdMktRpt

	@UscrdMktRpt.setter
	def UscrdMktRpt(self, value):
		self._UscrdMktRpt = value if type(value) != base_types.auto else self.make_default("UscrdMktRpt")

	@UscrdMktRpt.deleter
	def UscrdMktRpt(self):
		del self._UscrdMktRpt
		self._UscrdMktRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptHdr', type=MoneyMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UscrdMktRpt', type=UnsecuredMarketReport4Choice, min=1, max=1, mutex_group=None, array=False),
	))

