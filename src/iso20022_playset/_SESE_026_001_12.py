# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionReversalAdviceV12

class SESE_026_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.026.001.12"
		_docname = "sese.026.001.12"

		__slots__ = ["_SctiesSttlmTxRvslAdvc"]
		@property
		def SctiesSttlmTxRvslAdvc(self):
			return self._SctiesSttlmTxRvslAdvc

		@SctiesSttlmTxRvslAdvc.setter
		def SctiesSttlmTxRvslAdvc(self, value):
			self._SctiesSttlmTxRvslAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxRvslAdvc', SecuritiesSettlementTransactionReversalAdviceV12, False)

		@SctiesSttlmTxRvslAdvc.deleter
		def SctiesSttlmTxRvslAdvc(self):
			del self._SctiesSttlmTxRvslAdvc
			self._SctiesSttlmTxRvslAdvc = base_types.UninitialisedField(self, 'SctiesSttlmTxRvslAdvc', SecuritiesSettlementTransactionReversalAdviceV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxRvslAdvc', type=SecuritiesSettlementTransactionReversalAdviceV12, min=1, max=1, mutex_group=None, array=False),
		))