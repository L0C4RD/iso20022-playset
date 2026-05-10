from . import base_types
from .RequestToPayDebtorActivationCancellationRequestV02 import RequestToPayDebtorActivationCancellationRequestV02

class REDA_072_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqToPayDbtrActvtnCxlReq"]
		@property
		def ReqToPayDbtrActvtnCxlReq(self):
			return self._ReqToPayDbtrActvtnCxlReq

		@ReqToPayDbtrActvtnCxlReq.setter
		def ReqToPayDbtrActvtnCxlReq(self, value):
			self._ReqToPayDbtrActvtnCxlReq = value if type(value) != auto else self.make_default("ReqToPayDbtrActvtnCxlReq")

		@ReqToPayDbtrActvtnCxlReq.deleter
		def ReqToPayDbtrActvtnCxlReq(self):
			del self._ReqToPayDbtrActvtnCxlReq
			self._ReqToPayDbtrActvtnCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayDbtrActvtnCxlReq', type=RequestToPayDebtorActivationCancellationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

