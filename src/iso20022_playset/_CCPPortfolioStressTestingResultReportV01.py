# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ScenarioStressTestResult1
from . import SupplementaryData1

class CCPPortfolioStressTestingResultReportV01(base_types._BaseFieldType):

	__slots__ = ["_ScnroStrssTstRslt", "_SplmtryData"]
	@property
	def ScnroStrssTstRslt(self):
		return self._ScnroStrssTstRslt

	@ScnroStrssTstRslt.setter
	def ScnroStrssTstRslt(self, value):
		self._ScnroStrssTstRslt = value if value is not None else base_types.UninitialisedField(self, 'ScnroStrssTstRslt', ScenarioStressTestResult1, True)

	@ScnroStrssTstRslt.deleter
	def ScnroStrssTstRslt(self):
		del self._ScnroStrssTstRslt
		self._ScnroStrssTstRslt = base_types.UninitialisedField(self, 'ScnroStrssTstRslt', ScenarioStressTestResult1, True)

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
		base_types.FieldEntry(name='ScnroStrssTstRslt', type=ScenarioStressTestResult1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))