# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LiquidityStressTestResult1
from . import SupplementaryData1

class CCPLiquidityStressTestingResultReportV01(base_types._BaseFieldType):

	__slots__ = ["_LqdtyStrssTstRslt", "_SplmtryData"]
	@property
	def LqdtyStrssTstRslt(self):
		return self._LqdtyStrssTstRslt

	@LqdtyStrssTstRslt.setter
	def LqdtyStrssTstRslt(self, value):
		self._LqdtyStrssTstRslt = value if value is not None else base_types.UninitialisedField(self, 'LqdtyStrssTstRslt', LiquidityStressTestResult1, True)

	@LqdtyStrssTstRslt.deleter
	def LqdtyStrssTstRslt(self):
		del self._LqdtyStrssTstRslt
		self._LqdtyStrssTstRslt = base_types.UninitialisedField(self, 'LqdtyStrssTstRslt', LiquidityStressTestResult1, True)

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
		base_types.FieldEntry(name='LqdtyStrssTstRslt', type=LiquidityStressTestResult1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))