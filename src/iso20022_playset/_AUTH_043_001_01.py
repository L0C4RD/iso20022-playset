# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingReferenceDataIndexReportV01

class AUTH_043_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01"
		_docname = "auth.043.001.01"

		__slots__ = ["_FinInstrmRptgRefDataIndxRpt"]
		@property
		def FinInstrmRptgRefDataIndxRpt(self):
			return self._FinInstrmRptgRefDataIndxRpt

		@FinInstrmRptgRefDataIndxRpt.setter
		def FinInstrmRptgRefDataIndxRpt(self, value):
			self._FinInstrmRptgRefDataIndxRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgRefDataIndxRpt', FinancialInstrumentReportingReferenceDataIndexReportV01, False)

		@FinInstrmRptgRefDataIndxRpt.deleter
		def FinInstrmRptgRefDataIndxRpt(self):
			del self._FinInstrmRptgRefDataIndxRpt
			self._FinInstrmRptgRefDataIndxRpt = base_types.UninitialisedField(self, 'FinInstrmRptgRefDataIndxRpt', FinancialInstrumentReportingReferenceDataIndexReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgRefDataIndxRpt', type=FinancialInstrumentReportingReferenceDataIndexReportV01, min=1, max=1, mutex_group=None, array=False),
		))