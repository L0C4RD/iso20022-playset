# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingInstrumentClassificationReportV01 import FinancialInstrumentReportingInstrumentClassificationReportV01

class AUTH_050_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.050.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgInstrmClssfctnRpt"]
		@property
		def FinInstrmRptgInstrmClssfctnRpt(self):
			return self._FinInstrmRptgInstrmClssfctnRpt

		@FinInstrmRptgInstrmClssfctnRpt.setter
		def FinInstrmRptgInstrmClssfctnRpt(self, value):
			self._FinInstrmRptgInstrmClssfctnRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgInstrmClssfctnRpt")

		@FinInstrmRptgInstrmClssfctnRpt.deleter
		def FinInstrmRptgInstrmClssfctnRpt(self):
			del self._FinInstrmRptgInstrmClssfctnRpt
			self._FinInstrmRptgInstrmClssfctnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgInstrmClssfctnRpt', type=FinancialInstrumentReportingInstrumentClassificationReportV01, min=1, max=1, mutex_group=None, array=False),
		))