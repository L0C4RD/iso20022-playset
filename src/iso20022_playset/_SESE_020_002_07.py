# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionCancellationRequest002V07

class SESE_020_002_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.020.002.07"
		_docname = "sese.020.002.07"

		__slots__ = ["_SctiesTxCxlReq"]
		@property
		def SctiesTxCxlReq(self):
			return self._SctiesTxCxlReq

		@SctiesTxCxlReq.setter
		def SctiesTxCxlReq(self, value):
			self._SctiesTxCxlReq = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxCxlReq', SecuritiesTransactionCancellationRequest002V07, False)

		@SctiesTxCxlReq.deleter
		def SctiesTxCxlReq(self):
			del self._SctiesTxCxlReq
			self._SctiesTxCxlReq = base_types.UninitialisedField(self, 'SctiesTxCxlReq', SecuritiesTransactionCancellationRequest002V07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReq', type=SecuritiesTransactionCancellationRequest002V07, min=1, max=1, mutex_group=None, array=False),
		))