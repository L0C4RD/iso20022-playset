# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingReportingTransactionStatusAdviceV02

class AUTH_084_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02"
		_docname = "auth.084.001.02"

		__slots__ = ["_SctiesFincgRptgTxStsAdvc"]
		@property
		def SctiesFincgRptgTxStsAdvc(self):
			return self._SctiesFincgRptgTxStsAdvc

		@SctiesFincgRptgTxStsAdvc.setter
		def SctiesFincgRptgTxStsAdvc(self, value):
			self._SctiesFincgRptgTxStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgRptgTxStsAdvc', SecuritiesFinancingReportingTransactionStatusAdviceV02, False)

		@SctiesFincgRptgTxStsAdvc.deleter
		def SctiesFincgRptgTxStsAdvc(self):
			del self._SctiesFincgRptgTxStsAdvc
			self._SctiesFincgRptgTxStsAdvc = base_types.UninitialisedField(self, 'SctiesFincgRptgTxStsAdvc', SecuritiesFinancingReportingTransactionStatusAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxStsAdvc', type=SecuritiesFinancingReportingTransactionStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))