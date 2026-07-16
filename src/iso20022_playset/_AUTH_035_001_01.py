# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingTradingVolumeCapDataReportV01

class AUTH_035_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01"
		_docname = "auth.035.001.01"

		__slots__ = ["_FinInstrmRptgTradgVolCapDataRpt"]
		@property
		def FinInstrmRptgTradgVolCapDataRpt(self):
			return self._FinInstrmRptgTradgVolCapDataRpt

		@FinInstrmRptgTradgVolCapDataRpt.setter
		def FinInstrmRptgTradgVolCapDataRpt(self, value):
			self._FinInstrmRptgTradgVolCapDataRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgTradgVolCapDataRpt', FinancialInstrumentReportingTradingVolumeCapDataReportV01, False)

		@FinInstrmRptgTradgVolCapDataRpt.deleter
		def FinInstrmRptgTradgVolCapDataRpt(self):
			del self._FinInstrmRptgTradgVolCapDataRpt
			self._FinInstrmRptgTradgVolCapDataRpt = base_types.UninitialisedField(self, 'FinInstrmRptgTradgVolCapDataRpt', FinancialInstrumentReportingTradingVolumeCapDataReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgTradgVolCapDataRpt', type=FinancialInstrumentReportingTradingVolumeCapDataReportV01, min=1, max=1, mutex_group=None, array=False),
		))