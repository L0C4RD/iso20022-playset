from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._MessageReportHeader4 import MessageReportHeader4

class FinancialInstrumentReportingStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_StsAdvc", "_SplmtryData"]
	@property
	def StsAdvc(self):
		return self._StsAdvc

	@StsAdvc.setter
	def StsAdvc(self, value):
		self._StsAdvc = value if type(value) != base_types.auto else self.make_default("StsAdvc")

	@StsAdvc.deleter
	def StsAdvc(self):
		del self._StsAdvc
		self._StsAdvc = None

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
		base_types.FieldEntry(name='StsAdvc', type=MessageReportHeader4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

