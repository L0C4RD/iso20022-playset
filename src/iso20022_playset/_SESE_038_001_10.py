# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionModificationRequestV10 import SecuritiesSettlementTransactionModificationRequestV10

class SESE_038_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxModReq"]
		@property
		def SctiesSttlmTxModReq(self):
			return self._SctiesSttlmTxModReq

		@SctiesSttlmTxModReq.setter
		def SctiesSttlmTxModReq(self, value):
			self._SctiesSttlmTxModReq = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxModReq")

		@SctiesSttlmTxModReq.deleter
		def SctiesSttlmTxModReq(self):
			del self._SctiesSttlmTxModReq
			self._SctiesSttlmTxModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxModReq', type=SecuritiesSettlementTransactionModificationRequestV10, min=1, max=1, mutex_group=None, array=False),
		))