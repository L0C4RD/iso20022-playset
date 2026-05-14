from . import base_types
from ._SecuritiesSettlementTransactionReversalAdviceV12 import SecuritiesSettlementTransactionReversalAdviceV12

class SESE_026_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxRvslAdvc"]
		@property
		def SctiesSttlmTxRvslAdvc(self):
			return self._SctiesSttlmTxRvslAdvc

		@SctiesSttlmTxRvslAdvc.setter
		def SctiesSttlmTxRvslAdvc(self, value):
			self._SctiesSttlmTxRvslAdvc = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxRvslAdvc")

		@SctiesSttlmTxRvslAdvc.deleter
		def SctiesSttlmTxRvslAdvc(self):
			del self._SctiesSttlmTxRvslAdvc
			self._SctiesSttlmTxRvslAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxRvslAdvc', type=SecuritiesSettlementTransactionReversalAdviceV12, min=1, max=1, mutex_group=None, array=False),
		))

