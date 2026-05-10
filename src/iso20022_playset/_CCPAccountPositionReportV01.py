from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._PositionAccount2 import PositionAccount2

class CCPAccountPositionReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_Prtfl"]
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
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if type(value) != base_types.auto else self.make_default("Prtfl")

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prtfl', type=PositionAccount2, min=1, max=None, mutex_group=None, array=True),
	))

