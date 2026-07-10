# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingEquityTradingActivityResultV03 import FinancialInstrumentReportingEquityTradingActivityResultV03

class AUTH_044_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.044.001.03"
		_docname = "auth.044.001.03"

		__slots__ = ["_FinInstrmRptgEqtyTradgActvtyRslt"]
		@property
		def FinInstrmRptgEqtyTradgActvtyRslt(self):
			return self._FinInstrmRptgEqtyTradgActvtyRslt

		@FinInstrmRptgEqtyTradgActvtyRslt.setter
		def FinInstrmRptgEqtyTradgActvtyRslt(self, value):
			self._FinInstrmRptgEqtyTradgActvtyRslt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgEqtyTradgActvtyRslt")

		@FinInstrmRptgEqtyTradgActvtyRslt.deleter
		def FinInstrmRptgEqtyTradgActvtyRslt(self):
			del self._FinInstrmRptgEqtyTradgActvtyRslt
			self._FinInstrmRptgEqtyTradgActvtyRslt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgEqtyTradgActvtyRslt', type=FinancialInstrumentReportingEquityTradingActivityResultV03, min=1, max=1, mutex_group=None, array=False),
		))