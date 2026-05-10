from . import base_types
from ._RequestToPayDebtorActivationRequestV02 import RequestToPayDebtorActivationRequestV02

class REDA_070_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqToPayDbtrActvtnReq"]
		@property
		def ReqToPayDbtrActvtnReq(self):
			return self._ReqToPayDbtrActvtnReq

		@ReqToPayDbtrActvtnReq.setter
		def ReqToPayDbtrActvtnReq(self, value):
			self._ReqToPayDbtrActvtnReq = value if type(value) != base_types.auto else self.make_default("ReqToPayDbtrActvtnReq")

		@ReqToPayDbtrActvtnReq.deleter
		def ReqToPayDbtrActvtnReq(self):
			del self._ReqToPayDbtrActvtnReq
			self._ReqToPayDbtrActvtnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayDbtrActvtnReq', type=RequestToPayDebtorActivationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

