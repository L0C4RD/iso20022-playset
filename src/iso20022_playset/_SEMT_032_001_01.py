# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionCancellationRequestQueryV01

class SEMT_032_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.032.001.01"
		_docname = "semt.032.001.01"

		__slots__ = ["_SctiesTxCxlReqQry"]
		@property
		def SctiesTxCxlReqQry(self):
			return self._SctiesTxCxlReqQry

		@SctiesTxCxlReqQry.setter
		def SctiesTxCxlReqQry(self, value):
			self._SctiesTxCxlReqQry = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxCxlReqQry', SecuritiesTransactionCancellationRequestQueryV01, False)

		@SctiesTxCxlReqQry.deleter
		def SctiesTxCxlReqQry(self):
			del self._SctiesTxCxlReqQry
			self._SctiesTxCxlReqQry = base_types.UninitialisedField(self, 'SctiesTxCxlReqQry', SecuritiesTransactionCancellationRequestQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReqQry', type=SecuritiesTransactionCancellationRequestQueryV01, min=1, max=1, mutex_group=None, array=False),
		))