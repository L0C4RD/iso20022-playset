from . import base_types
from ._SecuritiesTransactionCancellationRequestV08 import SecuritiesTransactionCancellationRequestV08

class SESE_020_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTxCxlReq"]
		@property
		def SctiesTxCxlReq(self):
			return self._SctiesTxCxlReq

		@SctiesTxCxlReq.setter
		def SctiesTxCxlReq(self, value):
			self._SctiesTxCxlReq = value if type(value) != base_types.auto else self.make_default("SctiesTxCxlReq")

		@SctiesTxCxlReq.deleter
		def SctiesTxCxlReq(self):
			del self._SctiesTxCxlReq
			self._SctiesTxCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReq', type=SecuritiesTransactionCancellationRequestV08, min=1, max=1, mutex_group=None, array=False),
		))

