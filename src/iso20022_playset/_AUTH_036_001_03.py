# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingReferenceDataDeltaReportV03 import FinancialInstrumentReportingReferenceDataDeltaReportV03

class AUTH_036_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.036.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgRefDataDltaRpt"]
		@property
		def FinInstrmRptgRefDataDltaRpt(self):
			return self._FinInstrmRptgRefDataDltaRpt

		@FinInstrmRptgRefDataDltaRpt.setter
		def FinInstrmRptgRefDataDltaRpt(self, value):
			self._FinInstrmRptgRefDataDltaRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgRefDataDltaRpt")

		@FinInstrmRptgRefDataDltaRpt.deleter
		def FinInstrmRptgRefDataDltaRpt(self):
			del self._FinInstrmRptgRefDataDltaRpt
			self._FinInstrmRptgRefDataDltaRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgRefDataDltaRpt', type=FinancialInstrumentReportingReferenceDataDeltaReportV03, min=1, max=1, mutex_group=None, array=False),
		))