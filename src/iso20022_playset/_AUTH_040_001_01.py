# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingEquityTradingActivityReportV01

class AUTH_040_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01"
		_docname = "auth.040.001.01"

		__slots__ = ["_FinInstrmRptgEqtyTradgActvtyRpt"]
		@property
		def FinInstrmRptgEqtyTradgActvtyRpt(self):
			return self._FinInstrmRptgEqtyTradgActvtyRpt

		@FinInstrmRptgEqtyTradgActvtyRpt.setter
		def FinInstrmRptgEqtyTradgActvtyRpt(self, value):
			self._FinInstrmRptgEqtyTradgActvtyRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgEqtyTradgActvtyRpt', FinancialInstrumentReportingEquityTradingActivityReportV01, False)

		@FinInstrmRptgEqtyTradgActvtyRpt.deleter
		def FinInstrmRptgEqtyTradgActvtyRpt(self):
			del self._FinInstrmRptgEqtyTradgActvtyRpt
			self._FinInstrmRptgEqtyTradgActvtyRpt = base_types.UninitialisedField(self, 'FinInstrmRptgEqtyTradgActvtyRpt', FinancialInstrumentReportingEquityTradingActivityReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgEqtyTradgActvtyRpt', type=FinancialInstrumentReportingEquityTradingActivityReportV01, min=1, max=1, mutex_group=None, array=False),
		))