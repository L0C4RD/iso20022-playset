from . import base_types
from ._SecuritiesSettlementTransactionConfirmationV12 import SecuritiesSettlementTransactionConfirmationV12

class SESE_025_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxConf"]
		@property
		def SctiesSttlmTxConf(self):
			return self._SctiesSttlmTxConf

		@SctiesSttlmTxConf.setter
		def SctiesSttlmTxConf(self, value):
			self._SctiesSttlmTxConf = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxConf")

		@SctiesSttlmTxConf.deleter
		def SctiesSttlmTxConf(self):
			del self._SctiesSttlmTxConf
			self._SctiesSttlmTxConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxConf', type=SecuritiesSettlementTransactionConfirmationV12, min=1, max=1, mutex_group=None, array=False),
		))

