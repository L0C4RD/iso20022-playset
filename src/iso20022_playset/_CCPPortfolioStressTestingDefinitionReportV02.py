# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ScenarioDefinition2
from . import SupplementaryData1

class CCPPortfolioStressTestingDefinitionReportV02(base_types._BaseFieldType):

	__slots__ = ["_ScnroDef", "_SplmtryData"]
	@property
	def ScnroDef(self):
		return self._ScnroDef

	@ScnroDef.setter
	def ScnroDef(self, value):
		self._ScnroDef = value if value is not None else base_types.UninitialisedField(self, 'ScnroDef', ScenarioDefinition2, True)

	@ScnroDef.deleter
	def ScnroDef(self):
		del self._ScnroDef
		self._ScnroDef = base_types.UninitialisedField(self, 'ScnroDef', ScenarioDefinition2, True)

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
		base_types.FieldEntry(name='ScnroDef', type=ScenarioDefinition2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))