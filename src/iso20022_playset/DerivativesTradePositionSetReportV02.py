from . import base_types
from .PositionSetAggregated2Choice import PositionSetAggregated2Choice
from .SupplementaryData1 import SupplementaryData1

class DerivativesTradePositionSetReportV02(base_types._BaseFieldType):

	__slots__ = ["_AggtdPos", "_SplmtryData"]
	@property
	def AggtdPos(self):
		return self._AggtdPos

	@AggtdPos.setter
	def AggtdPos(self, value):
		self._AggtdPos = value if type(value) != auto else self.make_default("AggtdPos")

	@AggtdPos.deleter
	def AggtdPos(self):
		del self._AggtdPos
		self._AggtdPos = None

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
		base_types.FieldEntry(name='AggtdPos', type=PositionSetAggregated2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

