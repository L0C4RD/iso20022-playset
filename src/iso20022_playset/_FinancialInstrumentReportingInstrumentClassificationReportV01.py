# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesInstrumentClassification2
from . import SupplementaryData1

class FinancialInstrumentReportingInstrumentClassificationReportV01(base_types._BaseFieldType):

	__slots__ = ["_InstrmClssfctn", "_SplmtryData"]
	@property
	def InstrmClssfctn(self):
		return self._InstrmClssfctn

	@InstrmClssfctn.setter
	def InstrmClssfctn(self, value):
		self._InstrmClssfctn = value if value is not None else base_types.UninitialisedField(self, 'InstrmClssfctn', SecuritiesInstrumentClassification2, True)

	@InstrmClssfctn.deleter
	def InstrmClssfctn(self):
		del self._InstrmClssfctn
		self._InstrmClssfctn = base_types.UninitialisedField(self, 'InstrmClssfctn', SecuritiesInstrumentClassification2, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrmClssfctn', type=SecuritiesInstrumentClassification2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))