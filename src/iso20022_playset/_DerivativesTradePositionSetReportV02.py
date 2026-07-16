# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositionSetAggregated2Choice
from . import SupplementaryData1

class DerivativesTradePositionSetReportV02(base_types._BaseFieldType):

	__slots__ = ["_AggtdPos", "_SplmtryData"]
	@property
	def AggtdPos(self):
		return self._AggtdPos

	@AggtdPos.setter
	def AggtdPos(self, value):
		self._AggtdPos = value if value is not None else base_types.UninitialisedField(self, 'AggtdPos', PositionSetAggregated2Choice, False)

	@AggtdPos.deleter
	def AggtdPos(self):
		del self._AggtdPos
		self._AggtdPos = base_types.UninitialisedField(self, 'AggtdPos', PositionSetAggregated2Choice, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtdPos', type=PositionSetAggregated2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))