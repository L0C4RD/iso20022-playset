# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CutOffData2
from . import NettingCutOffReportData2
from . import SupplementaryData1

class NettingCutOffReferenceDataReportV02(base_types._BaseFieldType):

	__slots__ = ["_PtcptNetgCutOffData", "_RptData", "_SplmtryData"]
	@property
	def PtcptNetgCutOffData(self):
		return self._PtcptNetgCutOffData

	@PtcptNetgCutOffData.setter
	def PtcptNetgCutOffData(self, value):
		self._PtcptNetgCutOffData = value if value is not None else base_types.UninitialisedField(self, 'PtcptNetgCutOffData', CutOffData2, True)

	@PtcptNetgCutOffData.deleter
	def PtcptNetgCutOffData(self):
		del self._PtcptNetgCutOffData
		self._PtcptNetgCutOffData = base_types.UninitialisedField(self, 'PtcptNetgCutOffData', CutOffData2, True)

	@property
	def RptData(self):
		return self._RptData

	@RptData.setter
	def RptData(self, value):
		self._RptData = value if value is not None else base_types.UninitialisedField(self, 'RptData', NettingCutOffReportData2, False)

	@RptData.deleter
	def RptData(self):
		del self._RptData
		self._RptData = base_types.UninitialisedField(self, 'RptData', NettingCutOffReportData2, False)

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
		base_types.FieldEntry(name='PtcptNetgCutOffData', type=CutOffData2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptData', type=NettingCutOffReportData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))