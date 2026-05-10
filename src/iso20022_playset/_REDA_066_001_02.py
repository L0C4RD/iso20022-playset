from . import base_types
from ._RequestToPayCreditorEnrolmentRequestV02 import RequestToPayCreditorEnrolmentRequestV02

class REDA_066_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqToPayCdtrEnrlmntReq"]
		@property
		def ReqToPayCdtrEnrlmntReq(self):
			return self._ReqToPayCdtrEnrlmntReq

		@ReqToPayCdtrEnrlmntReq.setter
		def ReqToPayCdtrEnrlmntReq(self, value):
			self._ReqToPayCdtrEnrlmntReq = value if type(value) != base_types.auto else self.make_default("ReqToPayCdtrEnrlmntReq")

		@ReqToPayCdtrEnrlmntReq.deleter
		def ReqToPayCdtrEnrlmntReq(self):
			del self._ReqToPayCdtrEnrlmntReq
			self._ReqToPayCdtrEnrlmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayCdtrEnrlmntReq', type=RequestToPayCreditorEnrolmentRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

