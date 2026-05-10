from . import base_types
from ._SecuritiesSettlementTransactionAllegementReport002V10 import SecuritiesSettlementTransactionAllegementReport002V10

class SEMT_019_002_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxAllgmtRpt"]
		@property
		def SctiesSttlmTxAllgmtRpt(self):
			return self._SctiesSttlmTxAllgmtRpt

		@SctiesSttlmTxAllgmtRpt.setter
		def SctiesSttlmTxAllgmtRpt(self, value):
			self._SctiesSttlmTxAllgmtRpt = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxAllgmtRpt")

		@SctiesSttlmTxAllgmtRpt.deleter
		def SctiesSttlmTxAllgmtRpt(self):
			del self._SctiesSttlmTxAllgmtRpt
			self._SctiesSttlmTxAllgmtRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAllgmtRpt', type=SecuritiesSettlementTransactionAllegementReport002V10, min=1, max=1, mutex_group=None, array=False),
		))

