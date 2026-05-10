from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .SecuredMarketReport4Choice import SecuredMarketReport4Choice
from .MoneyMarketReportHeader1 import MoneyMarketReportHeader1

class MoneyMarketSecuredMarketStatisticalReportV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_ScrdMktRpt", "_RptHdr"]
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
	def ScrdMktRpt(self):
		return self._ScrdMktRpt

	@ScrdMktRpt.setter
	def ScrdMktRpt(self, value):
		self._ScrdMktRpt = value if type(value) != base_types.auto else self.make_default("ScrdMktRpt")

	@ScrdMktRpt.deleter
	def ScrdMktRpt(self):
		del self._ScrdMktRpt
		self._ScrdMktRpt = None

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
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ScrdMktRpt', type=SecuredMarketReport4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptHdr', type=MoneyMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
	))

