# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionStatusAdviceV13

class SESE_024_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13"
		_docname = "sese.024.001.13"

		__slots__ = ["_SctiesSttlmTxStsAdvc"]
		@property
		def SctiesSttlmTxStsAdvc(self):
			return self._SctiesSttlmTxStsAdvc

		@SctiesSttlmTxStsAdvc.setter
		def SctiesSttlmTxStsAdvc(self, value):
			self._SctiesSttlmTxStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxStsAdvc', SecuritiesSettlementTransactionStatusAdviceV13, False)

		@SctiesSttlmTxStsAdvc.deleter
		def SctiesSttlmTxStsAdvc(self):
			del self._SctiesSttlmTxStsAdvc
			self._SctiesSttlmTxStsAdvc = base_types.UninitialisedField(self, 'SctiesSttlmTxStsAdvc', SecuritiesSettlementTransactionStatusAdviceV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxStsAdvc', type=SecuritiesSettlementTransactionStatusAdviceV13, min=1, max=1, mutex_group=None, array=False),
		))