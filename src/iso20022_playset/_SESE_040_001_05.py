# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionCounterpartyResponseV05

class SESE_040_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.040.001.05"
		_docname = "sese.040.001.05"

		__slots__ = ["_SctiesSttlmTxCtrPtyRspn"]
		@property
		def SctiesSttlmTxCtrPtyRspn(self):
			return self._SctiesSttlmTxCtrPtyRspn

		@SctiesSttlmTxCtrPtyRspn.setter
		def SctiesSttlmTxCtrPtyRspn(self, value):
			self._SctiesSttlmTxCtrPtyRspn = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxCtrPtyRspn', SecuritiesSettlementTransactionCounterpartyResponseV05, False)

		@SctiesSttlmTxCtrPtyRspn.deleter
		def SctiesSttlmTxCtrPtyRspn(self):
			del self._SctiesSttlmTxCtrPtyRspn
			self._SctiesSttlmTxCtrPtyRspn = base_types.UninitialisedField(self, 'SctiesSttlmTxCtrPtyRspn', SecuritiesSettlementTransactionCounterpartyResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxCtrPtyRspn', type=SecuritiesSettlementTransactionCounterpartyResponseV05, min=1, max=1, mutex_group=None, array=False),
		))