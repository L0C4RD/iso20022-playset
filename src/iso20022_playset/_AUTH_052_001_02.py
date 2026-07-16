# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingReportingTransactionReportV02

class AUTH_052_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02"
		_docname = "auth.052.001.02"

		__slots__ = ["_SctiesFincgRptgTxRpt"]
		@property
		def SctiesFincgRptgTxRpt(self):
			return self._SctiesFincgRptgTxRpt

		@SctiesFincgRptgTxRpt.setter
		def SctiesFincgRptgTxRpt(self, value):
			self._SctiesFincgRptgTxRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgRptgTxRpt', SecuritiesFinancingReportingTransactionReportV02, False)

		@SctiesFincgRptgTxRpt.deleter
		def SctiesFincgRptgTxRpt(self):
			del self._SctiesFincgRptgTxRpt
			self._SctiesFincgRptgTxRpt = base_types.UninitialisedField(self, 'SctiesFincgRptgTxRpt', SecuritiesFinancingReportingTransactionReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxRpt', type=SecuritiesFinancingReportingTransactionReportV02, min=1, max=1, mutex_group=None, array=False),
		))