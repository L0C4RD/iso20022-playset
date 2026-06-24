# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingReferenceDataIndexReportV01 import FinancialInstrumentReportingReferenceDataIndexReportV01

class AUTH_043_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.043.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgRefDataIndxRpt"]
		@property
		def FinInstrmRptgRefDataIndxRpt(self):
			return self._FinInstrmRptgRefDataIndxRpt

		@FinInstrmRptgRefDataIndxRpt.setter
		def FinInstrmRptgRefDataIndxRpt(self, value):
			self._FinInstrmRptgRefDataIndxRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgRefDataIndxRpt")

		@FinInstrmRptgRefDataIndxRpt.deleter
		def FinInstrmRptgRefDataIndxRpt(self):
			del self._FinInstrmRptgRefDataIndxRpt
			self._FinInstrmRptgRefDataIndxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgRefDataIndxRpt', type=FinancialInstrumentReportingReferenceDataIndexReportV01, min=1, max=1, mutex_group=None, array=False),
		))