import base_types
import SupplementaryData1
import BenchmarkReport1Choice

class FinancialBenchmarkReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_BchmkData"]
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
	def BchmkData(self):
		return self._BchmkData

	@BchmkData.setter
	def BchmkData(self, value):
		self._BchmkData = value if type(value) != auto else self.make_default("BchmkData")

	@BchmkData.deleter
	def BchmkData(self):
		del self._BchmkData
		self._BchmkData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BchmkData', type=BenchmarkReport1Choice, min=1, max=None, mutex_group=None, array=True),
	))

