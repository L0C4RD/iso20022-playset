# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositionSetReport3Choice
from . import SupplementaryData1

class SecuritiesFinancingReportingPositionSetReportV01(base_types._BaseFieldType):

	__slots__ = ["_AggtdPoss", "_SplmtryData"]
	@property
	def AggtdPoss(self):
		return self._AggtdPoss

	@AggtdPoss.setter
	def AggtdPoss(self, value):
		self._AggtdPoss = value if value is not None else base_types.UninitialisedField(self, 'AggtdPoss', PositionSetReport3Choice, False)

	@AggtdPoss.deleter
	def AggtdPoss(self):
		del self._AggtdPoss
		self._AggtdPoss = base_types.UninitialisedField(self, 'AggtdPoss', PositionSetReport3Choice, False)

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
		base_types.FieldEntry(name='AggtdPoss', type=PositionSetReport3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))