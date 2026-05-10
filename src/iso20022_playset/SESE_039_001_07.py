from . import base_types
from .SecuritiesSettlementTransactionModificationRequestStatusAdviceV07 import SecuritiesSettlementTransactionModificationRequestStatusAdviceV07

class SESE_039_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxModReqStsAdvc"]
		@property
		def SctiesSttlmTxModReqStsAdvc(self):
			return self._SctiesSttlmTxModReqStsAdvc

		@SctiesSttlmTxModReqStsAdvc.setter
		def SctiesSttlmTxModReqStsAdvc(self, value):
			self._SctiesSttlmTxModReqStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxModReqStsAdvc")

		@SctiesSttlmTxModReqStsAdvc.deleter
		def SctiesSttlmTxModReqStsAdvc(self):
			del self._SctiesSttlmTxModReqStsAdvc
			self._SctiesSttlmTxModReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxModReqStsAdvc', type=SecuritiesSettlementTransactionModificationRequestStatusAdviceV07, min=1, max=1, mutex_group=None, array=False),
		))

