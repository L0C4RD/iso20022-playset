import base_types
import SecuritiesSettlementTransactionModificationRequest002V09

class SESE_038_002_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxModReq"]
		@property
		def SctiesSttlmTxModReq(self):
			return self._SctiesSttlmTxModReq

		@SctiesSttlmTxModReq.setter
		def SctiesSttlmTxModReq(self, value):
			self._SctiesSttlmTxModReq = value if type(value) != auto else self.make_default("SctiesSttlmTxModReq")

		@SctiesSttlmTxModReq.deleter
		def SctiesSttlmTxModReq(self):
			del self._SctiesSttlmTxModReq
			self._SctiesSttlmTxModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxModReq', type=SecuritiesSettlementTransactionModificationRequest002V09, min=1, max=1, mutex_group=None, array=False),
		))

