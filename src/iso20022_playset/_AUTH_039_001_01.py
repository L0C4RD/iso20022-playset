# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingNonWorkingDayReportV01

class AUTH_039_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.039.001.01"
		_docname = "auth.039.001.01"

		__slots__ = ["_FinInstrmRptgNonWorkgDayRpt"]
		@property
		def FinInstrmRptgNonWorkgDayRpt(self):
			return self._FinInstrmRptgNonWorkgDayRpt

		@FinInstrmRptgNonWorkgDayRpt.setter
		def FinInstrmRptgNonWorkgDayRpt(self, value):
			self._FinInstrmRptgNonWorkgDayRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgNonWorkgDayRpt', FinancialInstrumentReportingNonWorkingDayReportV01, False)

		@FinInstrmRptgNonWorkgDayRpt.deleter
		def FinInstrmRptgNonWorkgDayRpt(self):
			del self._FinInstrmRptgNonWorkgDayRpt
			self._FinInstrmRptgNonWorkgDayRpt = base_types.UninitialisedField(self, 'FinInstrmRptgNonWorkgDayRpt', FinancialInstrumentReportingNonWorkingDayReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgNonWorkgDayRpt', type=FinancialInstrumentReportingNonWorkingDayReportV01, min=1, max=1, mutex_group=None, array=False),
		))