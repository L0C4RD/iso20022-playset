# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionInstructionV13 import SecuritiesSettlementTransactionInstructionV13

class SESE_023_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.023.001.13"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

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
			base_types.FieldEntry(name='SctiesSttlmTxInstr', type=SecuritiesSettlementTransactionInstructionV13, min=1, max=1, mutex_group=None, array=False),
		))