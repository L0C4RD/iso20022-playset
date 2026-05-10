from . import base_types
from ._SecuritiesTransactionCancellationRequestStatusAdvice002V07 import SecuritiesTransactionCancellationRequestStatusAdvice002V07

class SESE_027_002_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTxCxlReqStsAdvc"]
		@property
		def SctiesTxCxlReqStsAdvc(self):
			return self._SctiesTxCxlReqStsAdvc

		@SctiesTxCxlReqStsAdvc.setter
		def SctiesTxCxlReqStsAdvc(self, value):
			self._SctiesTxCxlReqStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesTxCxlReqStsAdvc")

		@SctiesTxCxlReqStsAdvc.deleter
		def SctiesTxCxlReqStsAdvc(self):
			del self._SctiesTxCxlReqStsAdvc
			self._SctiesTxCxlReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReqStsAdvc', type=SecuritiesTransactionCancellationRequestStatusAdvice002V07, min=1, max=1, mutex_group=None, array=False),
		))

