# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ConcentrationAgent1
from . import SettlementAgent2
from . import SupplementaryData1

class CCPDailyCashFlowsReportV02(base_types._BaseFieldType):

	__slots__ = ["_CncntrtnAgt", "_SplmtryData", "_SttlmAgt"]
	@property
	def CncntrtnAgt(self):
		return self._CncntrtnAgt

	@CncntrtnAgt.setter
	def CncntrtnAgt(self, value):
		self._CncntrtnAgt = value if value is not None else base_types.UninitialisedField(self, 'CncntrtnAgt', ConcentrationAgent1, True)

	@CncntrtnAgt.deleter
	def CncntrtnAgt(self):
		del self._CncntrtnAgt
		self._CncntrtnAgt = base_types.UninitialisedField(self, 'CncntrtnAgt', ConcentrationAgent1, True)

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

	@property
	def SttlmAgt(self):
		return self._SttlmAgt

	@SttlmAgt.setter
	def SttlmAgt(self, value):
		self._SttlmAgt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAgt', SettlementAgent2, True)

	@SttlmAgt.deleter
	def SttlmAgt(self):
		del self._SttlmAgt
		self._SttlmAgt = base_types.UninitialisedField(self, 'SttlmAgt', SettlementAgent2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CncntrtnAgt', type=ConcentrationAgent1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmAgt', type=SettlementAgent2, min=1, max=None, mutex_group=None, array=True),
	))