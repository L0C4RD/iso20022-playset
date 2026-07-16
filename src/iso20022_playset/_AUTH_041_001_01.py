# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingNonEquityTradingActivityReportV01

class AUTH_041_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01"
		_docname = "auth.041.001.01"

		__slots__ = ["_FinInstrmRptgNonEqtyTradgActvtyRpt"]
		@property
		def FinInstrmRptgNonEqtyTradgActvtyRpt(self):
			return self._FinInstrmRptgNonEqtyTradgActvtyRpt

		@FinInstrmRptgNonEqtyTradgActvtyRpt.setter
		def FinInstrmRptgNonEqtyTradgActvtyRpt(self, value):
			self._FinInstrmRptgNonEqtyTradgActvtyRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgNonEqtyTradgActvtyRpt', FinancialInstrumentReportingNonEquityTradingActivityReportV01, False)

		@FinInstrmRptgNonEqtyTradgActvtyRpt.deleter
		def FinInstrmRptgNonEqtyTradgActvtyRpt(self):
			del self._FinInstrmRptgNonEqtyTradgActvtyRpt
			self._FinInstrmRptgNonEqtyTradgActvtyRpt = base_types.UninitialisedField(self, 'FinInstrmRptgNonEqtyTradgActvtyRpt', FinancialInstrumentReportingNonEquityTradingActivityReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgNonEqtyTradgActvtyRpt', type=FinancialInstrumentReportingNonEquityTradingActivityReportV01, min=1, max=1, mutex_group=None, array=False),
		))