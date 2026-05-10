from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .TradeData34Choice import TradeData34Choice

class SecuritiesFinancingReportingReconciliationStatusAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_RcncltnData", "_SplmtryData"]
	@property
	def RcncltnData(self):
		return self._RcncltnData

	@RcncltnData.setter
	def RcncltnData(self, value):
		self._RcncltnData = value if type(value) != auto else self.make_default("RcncltnData")

	@RcncltnData.deleter
	def RcncltnData(self):
		del self._RcncltnData
		self._RcncltnData = None

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
		base_types.FieldEntry(name='RcncltnData', type=TradeData34Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

