# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingTransactionReportV03 import FinancialInstrumentReportingTransactionReportV03

class AUTH_016_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03"
		_docname = "auth.016.001.03"

		__slots__ = ["_FinInstrmRptgTxRpt"]
		@property
		def FinInstrmRptgTxRpt(self):
			return self._FinInstrmRptgTxRpt

		@FinInstrmRptgTxRpt.setter
		def FinInstrmRptgTxRpt(self, value):
			self._FinInstrmRptgTxRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgTxRpt")

		@FinInstrmRptgTxRpt.deleter
		def FinInstrmRptgTxRpt(self):
			del self._FinInstrmRptgTxRpt
			self._FinInstrmRptgTxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgTxRpt', type=FinancialInstrumentReportingTransactionReportV03, min=1, max=1, mutex_group=None, array=False),
		))