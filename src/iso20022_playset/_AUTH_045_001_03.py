# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingNonEquityTradingActivityResultV03 import FinancialInstrumentReportingNonEquityTradingActivityResultV03

class AUTH_045_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.045.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgNonEqtyTradgActvtyRslt"]
		@property
		def FinInstrmRptgNonEqtyTradgActvtyRslt(self):
			return self._FinInstrmRptgNonEqtyTradgActvtyRslt

		@FinInstrmRptgNonEqtyTradgActvtyRslt.setter
		def FinInstrmRptgNonEqtyTradgActvtyRslt(self, value):
			self._FinInstrmRptgNonEqtyTradgActvtyRslt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgNonEqtyTradgActvtyRslt")

		@FinInstrmRptgNonEqtyTradgActvtyRslt.deleter
		def FinInstrmRptgNonEqtyTradgActvtyRslt(self):
			del self._FinInstrmRptgNonEqtyTradgActvtyRslt
			self._FinInstrmRptgNonEqtyTradgActvtyRslt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgNonEqtyTradgActvtyRslt', type=FinancialInstrumentReportingNonEquityTradingActivityResultV03, min=1, max=1, mutex_group=None, array=False),
		))