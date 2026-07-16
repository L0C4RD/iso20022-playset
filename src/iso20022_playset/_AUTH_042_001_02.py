# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingInvalidReferenceDataReportV02

class AUTH_042_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02"
		_docname = "auth.042.001.02"

		__slots__ = ["_FinInstrmRptgInvldRefDataRpt"]
		@property
		def FinInstrmRptgInvldRefDataRpt(self):
			return self._FinInstrmRptgInvldRefDataRpt

		@FinInstrmRptgInvldRefDataRpt.setter
		def FinInstrmRptgInvldRefDataRpt(self, value):
			self._FinInstrmRptgInvldRefDataRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgInvldRefDataRpt', FinancialInstrumentReportingInvalidReferenceDataReportV02, False)

		@FinInstrmRptgInvldRefDataRpt.deleter
		def FinInstrmRptgInvldRefDataRpt(self):
			del self._FinInstrmRptgInvldRefDataRpt
			self._FinInstrmRptgInvldRefDataRpt = base_types.UninitialisedField(self, 'FinInstrmRptgInvldRefDataRpt', FinancialInstrumentReportingInvalidReferenceDataReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgInvldRefDataRpt', type=FinancialInstrumentReportingInvalidReferenceDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))