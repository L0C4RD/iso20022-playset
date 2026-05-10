from . import base_types
import SupplementaryData1
import MarketIdentification95

class FinancialInstrumentReportingMarketIdentificationCodeReportV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_MktId"]
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
	def MktId(self):
		return self._MktId

	@MktId.setter
	def MktId(self, value):
		self._MktId = value if type(value) != auto else self.make_default("MktId")

	@MktId.deleter
	def MktId(self):
		del self._MktId
		self._MktId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MktId', type=MarketIdentification95, min=1, max=None, mutex_group=None, array=True),
	))

