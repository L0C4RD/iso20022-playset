import base_types
import SupplementaryData1
import ScenarioStressTestResult1

class CCPPortfolioStressTestingResultReportV01(base_types._BaseFieldType):

	__slots__ = ["_ScnroStrssTstRslt", "_SplmtryData"]
	@property
	def ScnroStrssTstRslt(self):
		return self._ScnroStrssTstRslt

	@ScnroStrssTstRslt.setter
	def ScnroStrssTstRslt(self, value):
		self._ScnroStrssTstRslt = value if type(value) != auto else self.make_default("ScnroStrssTstRslt")

	@ScnroStrssTstRslt.deleter
	def ScnroStrssTstRslt(self):
		del self._ScnroStrssTstRslt
		self._ScnroStrssTstRslt = None

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
		base_types.FieldEntry(name='ScnroStrssTstRslt', type=ScenarioStressTestResult1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

