import base_types
import SupplementaryData1
import LiquidityStressTestResult1

class CCPLiquidityStressTestingResultReportV01(base_types._BaseFieldType):

	__slots__ = ["_LqdtyStrssTstRslt", "_SplmtryData"]
	@property
	def LqdtyStrssTstRslt(self):
		return self._LqdtyStrssTstRslt

	@LqdtyStrssTstRslt.setter
	def LqdtyStrssTstRslt(self, value):
		self._LqdtyStrssTstRslt = value if type(value) != auto else self.make_default("LqdtyStrssTstRslt")

	@LqdtyStrssTstRslt.deleter
	def LqdtyStrssTstRslt(self):
		del self._LqdtyStrssTstRslt
		self._LqdtyStrssTstRslt = None

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
		base_types.FieldEntry(name='LqdtyStrssTstRslt', type=LiquidityStressTestResult1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

