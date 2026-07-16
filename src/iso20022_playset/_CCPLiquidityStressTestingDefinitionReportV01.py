# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LiquidityStressScenarioDefinition1
from . import SupplementaryData1

class CCPLiquidityStressTestingDefinitionReportV01(base_types._BaseFieldType):

	__slots__ = ["_LqdtyStrssScnroDef", "_SplmtryData"]
	@property
	def LqdtyStrssScnroDef(self):
		return self._LqdtyStrssScnroDef

	@LqdtyStrssScnroDef.setter
	def LqdtyStrssScnroDef(self, value):
		self._LqdtyStrssScnroDef = value if value is not None else base_types.UninitialisedField(self, 'LqdtyStrssScnroDef', LiquidityStressScenarioDefinition1, True)

	@LqdtyStrssScnroDef.deleter
	def LqdtyStrssScnroDef(self):
		del self._LqdtyStrssScnroDef
		self._LqdtyStrssScnroDef = base_types.UninitialisedField(self, 'LqdtyStrssScnroDef', LiquidityStressScenarioDefinition1, True)

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
		base_types.FieldEntry(name='LqdtyStrssScnroDef', type=LiquidityStressScenarioDefinition1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))