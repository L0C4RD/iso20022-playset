from . import base_types
import ConcentrationAgent1
import SupplementaryData1
import SettlementAgent2

class CCPDailyCashFlowsReportV02(base_types._BaseFieldType):

	__slots__ = ["_SttlmAgt", "_CncntrtnAgt", "_SplmtryData"]
	@property
	def SttlmAgt(self):
		return self._SttlmAgt

	@SttlmAgt.setter
	def SttlmAgt(self, value):
		self._SttlmAgt = value if type(value) != auto else self.make_default("SttlmAgt")

	@SttlmAgt.deleter
	def SttlmAgt(self):
		del self._SttlmAgt
		self._SttlmAgt = None

	@property
	def CncntrtnAgt(self):
		return self._CncntrtnAgt

	@CncntrtnAgt.setter
	def CncntrtnAgt(self, value):
		self._CncntrtnAgt = value if type(value) != auto else self.make_default("CncntrtnAgt")

	@CncntrtnAgt.deleter
	def CncntrtnAgt(self):
		del self._CncntrtnAgt
		self._CncntrtnAgt = None

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
		base_types.FieldEntry(name='SttlmAgt', type=SettlementAgent2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CncntrtnAgt', type=ConcentrationAgent1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

