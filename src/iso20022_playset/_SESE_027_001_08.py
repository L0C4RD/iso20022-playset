# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionCancellationRequestStatusAdviceV08

class SESE_027_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.027.001.08"
		_docname = "sese.027.001.08"

		__slots__ = ["_SctiesTxCxlReqStsAdvc"]
		@property
		def SctiesTxCxlReqStsAdvc(self):
			return self._SctiesTxCxlReqStsAdvc

		@SctiesTxCxlReqStsAdvc.setter
		def SctiesTxCxlReqStsAdvc(self, value):
			self._SctiesTxCxlReqStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxCxlReqStsAdvc', SecuritiesTransactionCancellationRequestStatusAdviceV08, False)

		@SctiesTxCxlReqStsAdvc.deleter
		def SctiesTxCxlReqStsAdvc(self):
			del self._SctiesTxCxlReqStsAdvc
			self._SctiesTxCxlReqStsAdvc = base_types.UninitialisedField(self, 'SctiesTxCxlReqStsAdvc', SecuritiesTransactionCancellationRequestStatusAdviceV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReqStsAdvc', type=SecuritiesTransactionCancellationRequestStatusAdviceV08, min=1, max=1, mutex_group=None, array=False),
		))