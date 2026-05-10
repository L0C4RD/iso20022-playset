import base_types
import PositionSetReport3Choice
import SupplementaryData1

class SecuritiesFinancingReportingPositionSetReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_AggtdPoss"]
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
	def AggtdPoss(self):
		return self._AggtdPoss

	@AggtdPoss.setter
	def AggtdPoss(self, value):
		self._AggtdPoss = value if type(value) != auto else self.make_default("AggtdPoss")

	@AggtdPoss.deleter
	def AggtdPoss(self):
		del self._AggtdPoss
		self._AggtdPoss = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AggtdPoss', type=PositionSetReport3Choice, min=1, max=1, mutex_group=None, array=False),
	))

