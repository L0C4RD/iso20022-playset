from . import base_types
from ._SecuritiesSettlementTransactionGenerationNotificationV12 import SecuritiesSettlementTransactionGenerationNotificationV12

class SESE_032_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxGnrtnNtfctn"]
		@property
		def SctiesSttlmTxGnrtnNtfctn(self):
			return self._SctiesSttlmTxGnrtnNtfctn

		@SctiesSttlmTxGnrtnNtfctn.setter
		def SctiesSttlmTxGnrtnNtfctn(self, value):
			self._SctiesSttlmTxGnrtnNtfctn = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxGnrtnNtfctn")

		@SctiesSttlmTxGnrtnNtfctn.deleter
		def SctiesSttlmTxGnrtnNtfctn(self):
			del self._SctiesSttlmTxGnrtnNtfctn
			self._SctiesSttlmTxGnrtnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxGnrtnNtfctn', type=SecuritiesSettlementTransactionGenerationNotificationV12, min=1, max=1, mutex_group=None, array=False),
		))

