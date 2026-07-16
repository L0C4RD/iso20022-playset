# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesCountryIdentification2
from . import SupplementaryData1

class FinancialInstrumentReportingCountryCodeReportV01(base_types._BaseFieldType):

	__slots__ = ["_CtryData", "_SplmtryData"]
	@property
	def CtryData(self):
		return self._CtryData

	@CtryData.setter
	def CtryData(self, value):
		self._CtryData = value if value is not None else base_types.UninitialisedField(self, 'CtryData', SecuritiesCountryIdentification2, True)

	@CtryData.deleter
	def CtryData(self):
		del self._CtryData
		self._CtryData = base_types.UninitialisedField(self, 'CtryData', SecuritiesCountryIdentification2, True)

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
		base_types.FieldEntry(name='CtryData', type=SecuritiesCountryIdentification2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))