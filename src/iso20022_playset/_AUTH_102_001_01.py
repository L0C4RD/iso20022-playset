# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingCancellationReportV01 import FinancialInstrumentReportingCancellationReportV01

class AUTH_102_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.102.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_FinInstrmRptgCxlRpt"]
		@property
		def FinInstrmRptgCxlRpt(self):
			return self._FinInstrmRptgCxlRpt

		@FinInstrmRptgCxlRpt.setter
		def FinInstrmRptgCxlRpt(self, value):
			self._FinInstrmRptgCxlRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgCxlRpt")

		@FinInstrmRptgCxlRpt.deleter
		def FinInstrmRptgCxlRpt(self):
			del self._FinInstrmRptgCxlRpt
			self._FinInstrmRptgCxlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgCxlRpt', type=FinancialInstrumentReportingCancellationReportV01, min=1, max=1, mutex_group=None, array=False),
		))