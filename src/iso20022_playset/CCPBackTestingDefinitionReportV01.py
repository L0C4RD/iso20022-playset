import base_types
import BackTestingMethodology1
import SupplementaryData1

class CCPBackTestingDefinitionReportV01(base_types._BaseFieldType):

	__slots__ = ["_Mthdlgy", "_SplmtryData"]
	@property
	def Mthdlgy(self):
		return self._Mthdlgy

	@Mthdlgy.setter
	def Mthdlgy(self, value):
		self._Mthdlgy = value if type(value) != auto else self.make_default("Mthdlgy")

	@Mthdlgy.deleter
	def Mthdlgy(self):
		del self._Mthdlgy
		self._Mthdlgy = None

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
		base_types.FieldEntry(name='Mthdlgy', type=BackTestingMethodology1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

