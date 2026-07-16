# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingNonEquityTransparencyDataReportV03

class AUTH_033_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03"
		_docname = "auth.033.001.03"

		__slots__ = ["_FinInstrmRptgNonEqtyTrnsprncyDataRpt"]
		@property
		def FinInstrmRptgNonEqtyTrnsprncyDataRpt(self):
			return self._FinInstrmRptgNonEqtyTrnsprncyDataRpt

		@FinInstrmRptgNonEqtyTrnsprncyDataRpt.setter
		def FinInstrmRptgNonEqtyTrnsprncyDataRpt(self, value):
			self._FinInstrmRptgNonEqtyTrnsprncyDataRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgNonEqtyTrnsprncyDataRpt', FinancialInstrumentReportingNonEquityTransparencyDataReportV03, False)

		@FinInstrmRptgNonEqtyTrnsprncyDataRpt.deleter
		def FinInstrmRptgNonEqtyTrnsprncyDataRpt(self):
			del self._FinInstrmRptgNonEqtyTrnsprncyDataRpt
			self._FinInstrmRptgNonEqtyTrnsprncyDataRpt = base_types.UninitialisedField(self, 'FinInstrmRptgNonEqtyTrnsprncyDataRpt', FinancialInstrumentReportingNonEquityTransparencyDataReportV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgNonEqtyTrnsprncyDataRpt', type=FinancialInstrumentReportingNonEquityTransparencyDataReportV03, min=1, max=1, mutex_group=None, array=False),
		))