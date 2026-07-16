# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionInstruction002V11

class SESE_023_002_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.023.002.11"
		_docname = "sese.023.002.11"

		__slots__ = ["_SctiesSttlmTxInstr"]
		@property
		def SctiesSttlmTxInstr(self):
			return self._SctiesSttlmTxInstr

		@SctiesSttlmTxInstr.setter
		def SctiesSttlmTxInstr(self, value):
			self._SctiesSttlmTxInstr = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxInstr', SecuritiesSettlementTransactionInstruction002V11, False)

		@SctiesSttlmTxInstr.deleter
		def SctiesSttlmTxInstr(self):
			del self._SctiesSttlmTxInstr
			self._SctiesSttlmTxInstr = base_types.UninitialisedField(self, 'SctiesSttlmTxInstr', SecuritiesSettlementTransactionInstruction002V11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxInstr', type=SecuritiesSettlementTransactionInstruction002V11, min=1, max=1, mutex_group=None, array=False),
		))