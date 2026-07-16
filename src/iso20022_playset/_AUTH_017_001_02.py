# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingReferenceDataReportV02

class AUTH_017_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.017.001.02"
		_docname = "auth.017.001.02"

		__slots__ = ["_FinInstrmRptgRefDataRpt"]
		@property
		def FinInstrmRptgRefDataRpt(self):
			return self._FinInstrmRptgRefDataRpt

		@FinInstrmRptgRefDataRpt.setter
		def FinInstrmRptgRefDataRpt(self, value):
			self._FinInstrmRptgRefDataRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgRefDataRpt', FinancialInstrumentReportingReferenceDataReportV02, False)

		@FinInstrmRptgRefDataRpt.deleter
		def FinInstrmRptgRefDataRpt(self):
			del self._FinInstrmRptgRefDataRpt
			self._FinInstrmRptgRefDataRpt = base_types.UninitialisedField(self, 'FinInstrmRptgRefDataRpt', FinancialInstrumentReportingReferenceDataReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgRefDataRpt', type=FinancialInstrumentReportingReferenceDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))