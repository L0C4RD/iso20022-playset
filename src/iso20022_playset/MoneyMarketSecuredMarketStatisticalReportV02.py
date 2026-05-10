from . import base_types
import SupplementaryData1
import SecuredMarketReport4Choice
import MoneyMarketReportHeader1

class MoneyMarketSecuredMarketStatisticalReportV02(base_types._BaseFieldType):

	__slots__ = ["_RptHdr", "_ScrdMktRpt", "_SplmtryData"]
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
	def ScrdMktRpt(self):
		return self._ScrdMktRpt

	@ScrdMktRpt.setter
	def ScrdMktRpt(self, value):
		self._ScrdMktRpt = value if type(value) != auto else self.make_default("ScrdMktRpt")

	@ScrdMktRpt.deleter
	def ScrdMktRpt(self):
		del self._ScrdMktRpt
		self._ScrdMktRpt = None

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
		base_types.FieldEntry(name='RptHdr', type=MoneyMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScrdMktRpt', type=SecuredMarketReport4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

