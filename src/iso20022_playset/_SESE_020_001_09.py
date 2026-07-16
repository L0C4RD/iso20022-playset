# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionCancellationRequestV09

class SESE_020_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.020.001.09"
		_docname = "sese.020.001.09"

		__slots__ = ["_SctiesTxCxlReq"]
		@property
		def SctiesTxCxlReq(self):
			return self._SctiesTxCxlReq

		@SctiesTxCxlReq.setter
		def SctiesTxCxlReq(self, value):
			self._SctiesTxCxlReq = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxCxlReq', SecuritiesTransactionCancellationRequestV09, False)

		@SctiesTxCxlReq.deleter
		def SctiesTxCxlReq(self):
			del self._SctiesTxCxlReq
			self._SctiesTxCxlReq = base_types.UninitialisedField(self, 'SctiesTxCxlReq', SecuritiesTransactionCancellationRequestV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReq', type=SecuritiesTransactionCancellationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))