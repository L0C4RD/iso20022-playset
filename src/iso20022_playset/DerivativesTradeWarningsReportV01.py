import base_types
import SupplementaryData1
import StatisticsPerCounterparty16Choice

class DerivativesTradeWarningsReportV01(base_types._BaseFieldType):

	__slots__ = ["_WrnngsSttstcs", "_SplmtryData"]
	@property
	def WrnngsSttstcs(self):
		return self._WrnngsSttstcs

	@WrnngsSttstcs.setter
	def WrnngsSttstcs(self, value):
		self._WrnngsSttstcs = value if type(value) != auto else self.make_default("WrnngsSttstcs")

	@WrnngsSttstcs.deleter
	def WrnngsSttstcs(self):
		del self._WrnngsSttstcs
		self._WrnngsSttstcs = None

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
		base_types.FieldEntry(name='WrnngsSttstcs', type=StatisticsPerCounterparty16Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

