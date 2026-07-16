# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingInstrumentClassificationReportV01

class AUTH_050_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01"
		_docname = "auth.050.001.01"

		__slots__ = ["_FinInstrmRptgInstrmClssfctnRpt"]
		@property
		def FinInstrmRptgInstrmClssfctnRpt(self):
			return self._FinInstrmRptgInstrmClssfctnRpt

		@FinInstrmRptgInstrmClssfctnRpt.setter
		def FinInstrmRptgInstrmClssfctnRpt(self, value):
			self._FinInstrmRptgInstrmClssfctnRpt = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgInstrmClssfctnRpt', FinancialInstrumentReportingInstrumentClassificationReportV01, False)

		@FinInstrmRptgInstrmClssfctnRpt.deleter
		def FinInstrmRptgInstrmClssfctnRpt(self):
			del self._FinInstrmRptgInstrmClssfctnRpt
			self._FinInstrmRptgInstrmClssfctnRpt = base_types.UninitialisedField(self, 'FinInstrmRptgInstrmClssfctnRpt', FinancialInstrumentReportingInstrumentClassificationReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgInstrmClssfctnRpt', type=FinancialInstrumentReportingInstrumentClassificationReportV01, min=1, max=1, mutex_group=None, array=False),
		))