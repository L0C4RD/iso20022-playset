from . import base_types
import SecuritiesSettlementTransactionConfirmation002V11

class SESE_025_002_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxConf"]
		@property
		def SctiesSttlmTxConf(self):
			return self._SctiesSttlmTxConf

		@SctiesSttlmTxConf.setter
		def SctiesSttlmTxConf(self, value):
			self._SctiesSttlmTxConf = value if type(value) != auto else self.make_default("SctiesSttlmTxConf")

		@SctiesSttlmTxConf.deleter
		def SctiesSttlmTxConf(self):
			del self._SctiesSttlmTxConf
			self._SctiesSttlmTxConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxConf', type=SecuritiesSettlementTransactionConfirmation002V11, min=1, max=1, mutex_group=None, array=False),
		))

