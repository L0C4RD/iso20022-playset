# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingTradingVolumeCapResultReportV01 import FinancialInstrumentReportingTradingVolumeCapResultReportV01

class AUTH_053_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.053.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgTradgVolCapRsltRpt"]
		@property
		def FinInstrmRptgTradgVolCapRsltRpt(self):
			return self._FinInstrmRptgTradgVolCapRsltRpt

		@FinInstrmRptgTradgVolCapRsltRpt.setter
		def FinInstrmRptgTradgVolCapRsltRpt(self, value):
			self._FinInstrmRptgTradgVolCapRsltRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgTradgVolCapRsltRpt")

		@FinInstrmRptgTradgVolCapRsltRpt.deleter
		def FinInstrmRptgTradgVolCapRsltRpt(self):
			del self._FinInstrmRptgTradgVolCapRsltRpt
			self._FinInstrmRptgTradgVolCapRsltRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgTradgVolCapRsltRpt', type=FinancialInstrumentReportingTradingVolumeCapResultReportV01, min=1, max=1, mutex_group=None, array=False),
		))