import base_types
import SupplementaryData1
import StatisticsPerCounterparty19Choice

class DerivativesTradeReconciliationStatisticalReportV03(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_RcncltnSttstcs"]
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

	@property
	def RcncltnSttstcs(self):
		return self._RcncltnSttstcs

	@RcncltnSttstcs.setter
	def RcncltnSttstcs(self, value):
		self._RcncltnSttstcs = value if type(value) != auto else self.make_default("RcncltnSttstcs")

	@RcncltnSttstcs.deleter
	def RcncltnSttstcs(self):
		del self._RcncltnSttstcs
		self._RcncltnSttstcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnSttstcs', type=StatisticsPerCounterparty19Choice, min=1, max=1, mutex_group=None, array=False),
	))

