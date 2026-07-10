# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingInvalidReferenceDataReportV02 import FinancialInstrumentReportingInvalidReferenceDataReportV02

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
			self._FinInstrmRptgInvldRefDataRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgInvldRefDataRpt")

		@FinInstrmRptgInvldRefDataRpt.deleter
		def FinInstrmRptgInvldRefDataRpt(self):
			del self._FinInstrmRptgInvldRefDataRpt
			self._FinInstrmRptgInvldRefDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgInvldRefDataRpt', type=FinancialInstrumentReportingInvalidReferenceDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))