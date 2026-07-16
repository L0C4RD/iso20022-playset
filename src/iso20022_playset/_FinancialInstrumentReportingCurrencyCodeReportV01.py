# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesCurrencyIdentification2
from . import SupplementaryData1

class FinancialInstrumentReportingCurrencyCodeReportV01(base_types._BaseFieldType):

	__slots__ = ["_CcyData", "_SplmtryData"]
	@property
	def CcyData(self):
		return self._CcyData

	@CcyData.setter
	def CcyData(self, value):
		self._CcyData = value if value is not None else base_types.UninitialisedField(self, 'CcyData', SecuritiesCurrencyIdentification2, True)

	@CcyData.deleter
	def CcyData(self):
		del self._CcyData
		self._CcyData = base_types.UninitialisedField(self, 'CcyData', SecuritiesCurrencyIdentification2, True)

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
		base_types.FieldEntry(name='CcyData', type=SecuritiesCurrencyIdentification2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))