from . import base_types
from ._SecuritiesCurrencyIdentification2 import SecuritiesCurrencyIdentification2
from ._SupplementaryData1 import SupplementaryData1

class FinancialInstrumentReportingCurrencyCodeReportV01(base_types._BaseFieldType):

	__slots__ = ["_CcyData", "_SplmtryData"]
	@property
	def CcyData(self):
		return self._CcyData

	@CcyData.setter
	def CcyData(self, value):
		self._CcyData = value if type(value) != base_types.auto else self.make_default("CcyData")

	@CcyData.deleter
	def CcyData(self):
		del self._CcyData
		self._CcyData = None

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
		base_types.FieldEntry(name='CcyData', type=SecuritiesCurrencyIdentification2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

