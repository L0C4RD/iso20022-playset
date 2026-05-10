from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .NettingCutOffReportData2 import NettingCutOffReportData2
from .CutOffData2 import CutOffData2

class NettingCutOffReferenceDataReportV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_RptData", "_PtcptNetgCutOffData"]
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
	def RptData(self):
		return self._RptData

	@RptData.setter
	def RptData(self, value):
		self._RptData = value if type(value) != base_types.auto else self.make_default("RptData")

	@RptData.deleter
	def RptData(self):
		del self._RptData
		self._RptData = None

	@property
	def PtcptNetgCutOffData(self):
		return self._PtcptNetgCutOffData

	@PtcptNetgCutOffData.setter
	def PtcptNetgCutOffData(self, value):
		self._PtcptNetgCutOffData = value if type(value) != base_types.auto else self.make_default("PtcptNetgCutOffData")

	@PtcptNetgCutOffData.deleter
	def PtcptNetgCutOffData(self):
		del self._PtcptNetgCutOffData
		self._PtcptNetgCutOffData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptData', type=NettingCutOffReportData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtcptNetgCutOffData', type=CutOffData2, min=1, max=None, mutex_group=None, array=True),
	))

