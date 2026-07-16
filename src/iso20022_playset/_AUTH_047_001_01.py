# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingCountryCodeReportV01

class AUTH_047_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01"
		_docname = "auth.047.001.01"

		__slots__ = ["_FinInstrmRptgCtryCdRpt"]
		@property
		def FinInstrmRptgCtryCdRpt(self):
			return self._FinInstrmRptgCtryCdRpt

		@FinInstrmRptgCtryCdRpt.setter
		def FinInstrmRptgCtryCdRpt(self, value):
			self._FinInstrmRptgCtryCdRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgCtryCdRpt', FinancialInstrumentReportingCountryCodeReportV01, False)

		@FinInstrmRptgCtryCdRpt.deleter
		def FinInstrmRptgCtryCdRpt(self):
			del self._FinInstrmRptgCtryCdRpt
			self._FinInstrmRptgCtryCdRpt = base_types.UninitialisedField(self, 'FinInstrmRptgCtryCdRpt', FinancialInstrumentReportingCountryCodeReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgCtryCdRpt', type=FinancialInstrumentReportingCountryCodeReportV01, min=1, max=1, mutex_group=None, array=False),
		))