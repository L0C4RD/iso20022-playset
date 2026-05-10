from . import base_types
import MessageReportHeader4
import SupplementaryData1

class FinancialInstrumentReportingStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_StsAdvc"]
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
	def StsAdvc(self):
		return self._StsAdvc

	@StsAdvc.setter
	def StsAdvc(self, value):
		self._StsAdvc = value if type(value) != auto else self.make_default("StsAdvc")

	@StsAdvc.deleter
	def StsAdvc(self):
		del self._StsAdvc
		self._StsAdvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsAdvc', type=MessageReportHeader4, min=1, max=None, mutex_group=None, array=True),
	))

