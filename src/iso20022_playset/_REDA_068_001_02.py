from . import base_types
from ._RequestToPayCreditorEnrolmentCancellationRequestV02 import RequestToPayCreditorEnrolmentCancellationRequestV02

class REDA_068_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqToPayCdtrEnrlmntCxlReq"]
		@property
		def ReqToPayCdtrEnrlmntCxlReq(self):
			return self._ReqToPayCdtrEnrlmntCxlReq

		@ReqToPayCdtrEnrlmntCxlReq.setter
		def ReqToPayCdtrEnrlmntCxlReq(self, value):
			self._ReqToPayCdtrEnrlmntCxlReq = value if type(value) != base_types.auto else self.make_default("ReqToPayCdtrEnrlmntCxlReq")

		@ReqToPayCdtrEnrlmntCxlReq.deleter
		def ReqToPayCdtrEnrlmntCxlReq(self):
			del self._ReqToPayCdtrEnrlmntCxlReq
			self._ReqToPayCdtrEnrlmntCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayCdtrEnrlmntCxlReq', type=RequestToPayCreditorEnrolmentCancellationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

