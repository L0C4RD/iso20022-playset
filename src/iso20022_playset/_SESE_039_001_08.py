# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionModificationRequestStatusAdviceV08

class SESE_039_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.039.001.08"
		_docname = "sese.039.001.08"

		__slots__ = ["_SctiesSttlmTxModReqStsAdvc"]
		@property
		def SctiesSttlmTxModReqStsAdvc(self):
			return self._SctiesSttlmTxModReqStsAdvc

		@SctiesSttlmTxModReqStsAdvc.setter
		def SctiesSttlmTxModReqStsAdvc(self, value):
			self._SctiesSttlmTxModReqStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxModReqStsAdvc', SecuritiesSettlementTransactionModificationRequestStatusAdviceV08, False)

		@SctiesSttlmTxModReqStsAdvc.deleter
		def SctiesSttlmTxModReqStsAdvc(self):
			del self._SctiesSttlmTxModReqStsAdvc
			self._SctiesSttlmTxModReqStsAdvc = base_types.UninitialisedField(self, 'SctiesSttlmTxModReqStsAdvc', SecuritiesSettlementTransactionModificationRequestStatusAdviceV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxModReqStsAdvc', type=SecuritiesSettlementTransactionModificationRequestStatusAdviceV08, min=1, max=1, mutex_group=None, array=False),
		))