from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._StatisticsPerCounterparty18Choice import StatisticsPerCounterparty18Choice

class DerivativesTradeRejectionStatisticalReportV04(base_types._BaseFieldType):

	__slots__ = ["_RjctnSttstcs", "_SplmtryData"]
	@property
	def RjctnSttstcs(self):
		return self._RjctnSttstcs

	@RjctnSttstcs.setter
	def RjctnSttstcs(self, value):
		self._RjctnSttstcs = value if type(value) != base_types.auto else self.make_default("RjctnSttstcs")

	@RjctnSttstcs.deleter
	def RjctnSttstcs(self):
		del self._RjctnSttstcs
		self._RjctnSttstcs = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctnSttstcs', type=StatisticsPerCounterparty18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

