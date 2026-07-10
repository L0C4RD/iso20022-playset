# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionInstructionV12 import SecuritiesSettlementTransactionInstructionV12

class SESE_023_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.023.001.12"
		_docname = "sese.023.001.12"

		__slots__ = ["_SctiesSttlmTxInstr"]
		@property
		def SctiesSttlmTxInstr(self):
			return self._SctiesSttlmTxInstr

		@SctiesSttlmTxInstr.setter
		def SctiesSttlmTxInstr(self, value):
			self._SctiesSttlmTxInstr = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxInstr")

		@SctiesSttlmTxInstr.deleter
		def SctiesSttlmTxInstr(self):
			del self._SctiesSttlmTxInstr
			self._SctiesSttlmTxInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxInstr', type=SecuritiesSettlementTransactionInstructionV12, min=1, max=1, mutex_group=None, array=False),
		))