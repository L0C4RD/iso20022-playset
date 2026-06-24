# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingMarketIdentificationCodeReportV02 import FinancialInstrumentReportingMarketIdentificationCodeReportV02

class AUTH_049_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.049.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgMktIdCdRpt"]
		@property
		def FinInstrmRptgMktIdCdRpt(self):
			return self._FinInstrmRptgMktIdCdRpt

		@FinInstrmRptgMktIdCdRpt.setter
		def FinInstrmRptgMktIdCdRpt(self, value):
			self._FinInstrmRptgMktIdCdRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgMktIdCdRpt")

		@FinInstrmRptgMktIdCdRpt.deleter
		def FinInstrmRptgMktIdCdRpt(self):
			del self._FinInstrmRptgMktIdCdRpt
			self._FinInstrmRptgMktIdCdRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgMktIdCdRpt', type=FinancialInstrumentReportingMarketIdentificationCodeReportV02, min=1, max=1, mutex_group=None, array=False),
		))