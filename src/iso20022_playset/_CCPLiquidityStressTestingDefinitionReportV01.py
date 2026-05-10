from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._LiquidityStressScenarioDefinition1 import LiquidityStressScenarioDefinition1

class CCPLiquidityStressTestingDefinitionReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_LqdtyStrssScnroDef"]
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

	@property
	def LqdtyStrssScnroDef(self):
		return self._LqdtyStrssScnroDef

	@LqdtyStrssScnroDef.setter
	def LqdtyStrssScnroDef(self, value):
		self._LqdtyStrssScnroDef = value if type(value) != base_types.auto else self.make_default("LqdtyStrssScnroDef")

	@LqdtyStrssScnroDef.deleter
	def LqdtyStrssScnroDef(self):
		del self._LqdtyStrssScnroDef
		self._LqdtyStrssScnroDef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LqdtyStrssScnroDef', type=LiquidityStressScenarioDefinition1, min=1, max=None, mutex_group=None, array=True),
	))

