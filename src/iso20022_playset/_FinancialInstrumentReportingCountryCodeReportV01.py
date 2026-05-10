from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .SecuritiesCountryIdentification2 import SecuritiesCountryIdentification2

class FinancialInstrumentReportingCountryCodeReportV01(base_types._BaseFieldType):

	__slots__ = ["_CtryData", "_SplmtryData"]
	@property
	def CtryData(self):
		return self._CtryData

	@CtryData.setter
	def CtryData(self, value):
		self._CtryData = value if type(value) != base_types.auto else self.make_default("CtryData")

	@CtryData.deleter
	def CtryData(self):
		del self._CtryData
		self._CtryData = None

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
		base_types.FieldEntry(name='CtryData', type=SecuritiesCountryIdentification2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

