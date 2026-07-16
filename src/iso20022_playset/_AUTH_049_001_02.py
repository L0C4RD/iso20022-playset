# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingMarketIdentificationCodeReportV02

class AUTH_049_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02"
		_docname = "auth.049.001.02"

		__slots__ = ["_FinInstrmRptgMktIdCdRpt"]
		@property
		def FinInstrmRptgMktIdCdRpt(self):
			return self._FinInstrmRptgMktIdCdRpt

		@FinInstrmRptgMktIdCdRpt.setter
		def FinInstrmRptgMktIdCdRpt(self, value):
			self._FinInstrmRptgMktIdCdRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgMktIdCdRpt', FinancialInstrumentReportingMarketIdentificationCodeReportV02, False)

		@FinInstrmRptgMktIdCdRpt.deleter
		def FinInstrmRptgMktIdCdRpt(self):
			del self._FinInstrmRptgMktIdCdRpt
			self._FinInstrmRptgMktIdCdRpt = base_types.UninitialisedField(self, 'FinInstrmRptgMktIdCdRpt', FinancialInstrumentReportingMarketIdentificationCodeReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgMktIdCdRpt', type=FinancialInstrumentReportingMarketIdentificationCodeReportV02, min=1, max=1, mutex_group=None, array=False),
		))