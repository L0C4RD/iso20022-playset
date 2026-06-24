# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingCurrencyCodeReportV01 import FinancialInstrumentReportingCurrencyCodeReportV01

class AUTH_048_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.048.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgCcyCdRpt"]
		@property
		def FinInstrmRptgCcyCdRpt(self):
			return self._FinInstrmRptgCcyCdRpt

		@FinInstrmRptgCcyCdRpt.setter
		def FinInstrmRptgCcyCdRpt(self, value):
			self._FinInstrmRptgCcyCdRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgCcyCdRpt")

		@FinInstrmRptgCcyCdRpt.deleter
		def FinInstrmRptgCcyCdRpt(self):
			del self._FinInstrmRptgCcyCdRpt
			self._FinInstrmRptgCcyCdRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgCcyCdRpt', type=FinancialInstrumentReportingCurrencyCodeReportV01, min=1, max=1, mutex_group=None, array=False),
		))