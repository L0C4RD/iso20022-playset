# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingReferenceDataDeltaReportV03

class AUTH_036_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03"
		_docname = "auth.036.001.03"

		__slots__ = ["_FinInstrmRptgRefDataDltaRpt"]
		@property
		def FinInstrmRptgRefDataDltaRpt(self):
			return self._FinInstrmRptgRefDataDltaRpt

		@FinInstrmRptgRefDataDltaRpt.setter
		def FinInstrmRptgRefDataDltaRpt(self, value):
			self._FinInstrmRptgRefDataDltaRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgRefDataDltaRpt', FinancialInstrumentReportingReferenceDataDeltaReportV03, False)

		@FinInstrmRptgRefDataDltaRpt.deleter
		def FinInstrmRptgRefDataDltaRpt(self):
			del self._FinInstrmRptgRefDataDltaRpt
			self._FinInstrmRptgRefDataDltaRpt = base_types.UninitialisedField(self, 'FinInstrmRptgRefDataDltaRpt', FinancialInstrumentReportingReferenceDataDeltaReportV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgRefDataDltaRpt', type=FinancialInstrumentReportingReferenceDataDeltaReportV03, min=1, max=1, mutex_group=None, array=False),
		))