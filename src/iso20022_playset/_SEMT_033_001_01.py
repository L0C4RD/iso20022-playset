# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionCancellationRequestReportV01

class SEMT_033_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.033.001.01"
		_docname = "semt.033.001.01"

		__slots__ = ["_SctiesTxCxlReqRpt"]
		@property
		def SctiesTxCxlReqRpt(self):
			return self._SctiesTxCxlReqRpt

		@SctiesTxCxlReqRpt.setter
		def SctiesTxCxlReqRpt(self, value):
			self._SctiesTxCxlReqRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxCxlReqRpt', SecuritiesTransactionCancellationRequestReportV01, False)

		@SctiesTxCxlReqRpt.deleter
		def SctiesTxCxlReqRpt(self):
			del self._SctiesTxCxlReqRpt
			self._SctiesTxCxlReqRpt = base_types.UninitialisedField(self, 'SctiesTxCxlReqRpt', SecuritiesTransactionCancellationRequestReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReqRpt', type=SecuritiesTransactionCancellationRequestReportV01, min=1, max=1, mutex_group=None, array=False),
		))