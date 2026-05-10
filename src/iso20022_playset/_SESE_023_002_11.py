from . import base_types
from .SecuritiesSettlementTransactionInstruction002V11 import SecuritiesSettlementTransactionInstruction002V11

class SESE_023_002_11():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='SctiesSttlmTxInstr', type=SecuritiesSettlementTransactionInstruction002V11, min=1, max=1, mutex_group=None, array=False),
		))

