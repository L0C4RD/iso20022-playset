from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._PositionSetReport3Choice import PositionSetReport3Choice

class SecuritiesFinancingReportingPositionSetReportV01(base_types._BaseFieldType):

	__slots__ = ["_AggtdPoss", "_SplmtryData"]
	@property
	def AggtdPoss(self):
		return self._AggtdPoss

	@AggtdPoss.setter
	def AggtdPoss(self, value):
		self._AggtdPoss = value if type(value) != base_types.auto else self.make_default("AggtdPoss")

	@AggtdPoss.deleter
	def AggtdPoss(self):
		del self._AggtdPoss
		self._AggtdPoss = None

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
		base_types.FieldEntry(name='AggtdPoss', type=PositionSetReport3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

