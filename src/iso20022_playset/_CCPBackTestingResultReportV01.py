from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .MonthlyResult1 import MonthlyResult1

class CCPBackTestingResultReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_MnthlyRslt"]
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
	def MnthlyRslt(self):
		return self._MnthlyRslt

	@MnthlyRslt.setter
	def MnthlyRslt(self, value):
		self._MnthlyRslt = value if type(value) != base_types.auto else self.make_default("MnthlyRslt")

	@MnthlyRslt.deleter
	def MnthlyRslt(self):
		del self._MnthlyRslt
		self._MnthlyRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MnthlyRslt', type=MonthlyResult1, min=1, max=None, mutex_group=None, array=True),
	))

