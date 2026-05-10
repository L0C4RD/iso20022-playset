import base_types
import SecuritiesSettlementTransactionStatusAdvice002V12

class SESE_024_002_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxStsAdvc"]
		@property
		def SctiesSttlmTxStsAdvc(self):
			return self._SctiesSttlmTxStsAdvc

		@SctiesSttlmTxStsAdvc.setter
		def SctiesSttlmTxStsAdvc(self, value):
			self._SctiesSttlmTxStsAdvc = value if type(value) != auto else self.make_default("SctiesSttlmTxStsAdvc")

		@SctiesSttlmTxStsAdvc.deleter
		def SctiesSttlmTxStsAdvc(self):
			del self._SctiesSttlmTxStsAdvc
			self._SctiesSttlmTxStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxStsAdvc', type=SecuritiesSettlementTransactionStatusAdvice002V12, min=1, max=1, mutex_group=None, array=False),
		))

