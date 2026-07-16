# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingTradingVolumeCapResultReportV01

class AUTH_053_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01"
		_docname = "auth.053.001.01"

		__slots__ = ["_FinInstrmRptgTradgVolCapRsltRpt"]
		@property
		def FinInstrmRptgTradgVolCapRsltRpt(self):
			return self._FinInstrmRptgTradgVolCapRsltRpt

		@FinInstrmRptgTradgVolCapRsltRpt.setter
		def FinInstrmRptgTradgVolCapRsltRpt(self, value):
			self._FinInstrmRptgTradgVolCapRsltRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgTradgVolCapRsltRpt', FinancialInstrumentReportingTradingVolumeCapResultReportV01, False)

		@FinInstrmRptgTradgVolCapRsltRpt.deleter
		def FinInstrmRptgTradgVolCapRsltRpt(self):
			del self._FinInstrmRptgTradgVolCapRsltRpt
			self._FinInstrmRptgTradgVolCapRsltRpt = base_types.UninitialisedField(self, 'FinInstrmRptgTradgVolCapRsltRpt', FinancialInstrumentReportingTradingVolumeCapResultReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgTradgVolCapRsltRpt', type=FinancialInstrumentReportingTradingVolumeCapResultReportV01, min=1, max=1, mutex_group=None, array=False),
		))