from . import base_types
from .SecuritiesSettlementTransactionAllegementNotificationV11 import SecuritiesSettlementTransactionAllegementNotificationV11

class SESE_028_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxAllgmtNtfctn"]
		@property
		def SctiesSttlmTxAllgmtNtfctn(self):
			return self._SctiesSttlmTxAllgmtNtfctn

		@SctiesSttlmTxAllgmtNtfctn.setter
		def SctiesSttlmTxAllgmtNtfctn(self, value):
			self._SctiesSttlmTxAllgmtNtfctn = value if type(value) != auto else self.make_default("SctiesSttlmTxAllgmtNtfctn")

		@SctiesSttlmTxAllgmtNtfctn.deleter
		def SctiesSttlmTxAllgmtNtfctn(self):
			del self._SctiesSttlmTxAllgmtNtfctn
			self._SctiesSttlmTxAllgmtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAllgmtNtfctn', type=SecuritiesSettlementTransactionAllegementNotificationV11, min=1, max=1, mutex_group=None, array=False),
		))

