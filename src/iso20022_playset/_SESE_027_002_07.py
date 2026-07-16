# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionCancellationRequestStatusAdvice002V07

class SESE_027_002_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.027.002.07"
		_docname = "sese.027.002.07"

		__slots__ = ["_SctiesTxCxlReqStsAdvc"]
		@property
		def SctiesTxCxlReqStsAdvc(self):
			return self._SctiesTxCxlReqStsAdvc

		@SctiesTxCxlReqStsAdvc.setter
		def SctiesTxCxlReqStsAdvc(self, value):
			self._SctiesTxCxlReqStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxCxlReqStsAdvc', SecuritiesTransactionCancellationRequestStatusAdvice002V07, False)

		@SctiesTxCxlReqStsAdvc.deleter
		def SctiesTxCxlReqStsAdvc(self):
			del self._SctiesTxCxlReqStsAdvc
			self._SctiesTxCxlReqStsAdvc = base_types.UninitialisedField(self, 'SctiesTxCxlReqStsAdvc', SecuritiesTransactionCancellationRequestStatusAdvice002V07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReqStsAdvc', type=SecuritiesTransactionCancellationRequestStatusAdvice002V07, min=1, max=1, mutex_group=None, array=False),
		))