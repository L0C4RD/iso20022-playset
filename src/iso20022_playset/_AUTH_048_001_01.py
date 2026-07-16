# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingCurrencyCodeReportV01

class AUTH_048_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01"
		_docname = "auth.048.001.01"

		__slots__ = ["_FinInstrmRptgCcyCdRpt"]
		@property
		def FinInstrmRptgCcyCdRpt(self):
			return self._FinInstrmRptgCcyCdRpt

		@FinInstrmRptgCcyCdRpt.setter
		def FinInstrmRptgCcyCdRpt(self, value):
			self._FinInstrmRptgCcyCdRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgCcyCdRpt', FinancialInstrumentReportingCurrencyCodeReportV01, False)

		@FinInstrmRptgCcyCdRpt.deleter
		def FinInstrmRptgCcyCdRpt(self):
			del self._FinInstrmRptgCcyCdRpt
			self._FinInstrmRptgCcyCdRpt = base_types.UninitialisedField(self, 'FinInstrmRptgCcyCdRpt', FinancialInstrumentReportingCurrencyCodeReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgCcyCdRpt', type=FinancialInstrumentReportingCurrencyCodeReportV01, min=1, max=1, mutex_group=None, array=False),
		))