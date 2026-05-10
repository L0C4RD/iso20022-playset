from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .SecuritiesInstrumentClassification2 import SecuritiesInstrumentClassification2

class FinancialInstrumentReportingInstrumentClassificationReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_InstrmClssfctn"]
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
	def InstrmClssfctn(self):
		return self._InstrmClssfctn

	@InstrmClssfctn.setter
	def InstrmClssfctn(self, value):
		self._InstrmClssfctn = value if type(value) != base_types.auto else self.make_default("InstrmClssfctn")

	@InstrmClssfctn.deleter
	def InstrmClssfctn(self):
		del self._InstrmClssfctn
		self._InstrmClssfctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrmClssfctn', type=SecuritiesInstrumentClassification2, min=1, max=None, mutex_group=None, array=True),
	))

