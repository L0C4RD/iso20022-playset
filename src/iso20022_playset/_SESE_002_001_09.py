from . import base_types
from .TransferOutCancellationRequestV09 import TransferOutCancellationRequestV09

class SESE_002_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrfOutCxlReq"]
		@property
		def TrfOutCxlReq(self):
			return self._TrfOutCxlReq

		@TrfOutCxlReq.setter
		def TrfOutCxlReq(self, value):
			self._TrfOutCxlReq = value if type(value) != base_types.auto else self.make_default("TrfOutCxlReq")

		@TrfOutCxlReq.deleter
		def TrfOutCxlReq(self):
			del self._TrfOutCxlReq
			self._TrfOutCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfOutCxlReq', type=TransferOutCancellationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))

