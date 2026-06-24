# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingEquityTradingActivityReportV01 import FinancialInstrumentReportingEquityTradingActivityReportV01

class AUTH_040_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.040.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgEqtyTradgActvtyRpt"]
		@property
		def FinInstrmRptgEqtyTradgActvtyRpt(self):
			return self._FinInstrmRptgEqtyTradgActvtyRpt

		@FinInstrmRptgEqtyTradgActvtyRpt.setter
		def FinInstrmRptgEqtyTradgActvtyRpt(self, value):
			self._FinInstrmRptgEqtyTradgActvtyRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgEqtyTradgActvtyRpt")

		@FinInstrmRptgEqtyTradgActvtyRpt.deleter
		def FinInstrmRptgEqtyTradgActvtyRpt(self):
			del self._FinInstrmRptgEqtyTradgActvtyRpt
			self._FinInstrmRptgEqtyTradgActvtyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgEqtyTradgActvtyRpt', type=FinancialInstrumentReportingEquityTradingActivityReportV01, min=1, max=1, mutex_group=None, array=False),
		))