# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionCounterpartyResponse002V04 import SecuritiesSettlementTransactionCounterpartyResponse002V04

class SESE_040_002_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxCtrPtyRspn"]
		@property
		def SctiesSttlmTxCtrPtyRspn(self):
			return self._SctiesSttlmTxCtrPtyRspn

		@SctiesSttlmTxCtrPtyRspn.setter
		def SctiesSttlmTxCtrPtyRspn(self, value):
			self._SctiesSttlmTxCtrPtyRspn = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxCtrPtyRspn")

		@SctiesSttlmTxCtrPtyRspn.deleter
		def SctiesSttlmTxCtrPtyRspn(self):
			del self._SctiesSttlmTxCtrPtyRspn
			self._SctiesSttlmTxCtrPtyRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxCtrPtyRspn', type=SecuritiesSettlementTransactionCounterpartyResponse002V04, min=1, max=1, mutex_group=None, array=False),
		))