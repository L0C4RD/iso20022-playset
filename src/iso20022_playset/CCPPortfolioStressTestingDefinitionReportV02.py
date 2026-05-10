import base_types
import SupplementaryData1
import ScenarioDefinition2

class CCPPortfolioStressTestingDefinitionReportV02(base_types._BaseFieldType):

	__slots__ = ["_ScnroDef", "_SplmtryData"]
	@property
	def ScnroDef(self):
		return self._ScnroDef

	@ScnroDef.setter
	def ScnroDef(self, value):
		self._ScnroDef = value if type(value) != auto else self.make_default("ScnroDef")

	@ScnroDef.deleter
	def ScnroDef(self):
		del self._ScnroDef
		self._ScnroDef = None

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
		base_types.FieldEntry(name='ScnroDef', type=ScenarioDefinition2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

