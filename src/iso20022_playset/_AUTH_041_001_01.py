# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingNonEquityTradingActivityReportV01 import FinancialInstrumentReportingNonEquityTradingActivityReportV01

class AUTH_041_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.041.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgNonEqtyTradgActvtyRpt"]
		@property
		def FinInstrmRptgNonEqtyTradgActvtyRpt(self):
			return self._FinInstrmRptgNonEqtyTradgActvtyRpt

		@FinInstrmRptgNonEqtyTradgActvtyRpt.setter
		def FinInstrmRptgNonEqtyTradgActvtyRpt(self, value):
			self._FinInstrmRptgNonEqtyTradgActvtyRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgNonEqtyTradgActvtyRpt")

		@FinInstrmRptgNonEqtyTradgActvtyRpt.deleter
		def FinInstrmRptgNonEqtyTradgActvtyRpt(self):
			del self._FinInstrmRptgNonEqtyTradgActvtyRpt
			self._FinInstrmRptgNonEqtyTradgActvtyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgNonEqtyTradgActvtyRpt', type=FinancialInstrumentReportingNonEquityTradingActivityReportV01, min=1, max=1, mutex_group=None, array=False),
		))