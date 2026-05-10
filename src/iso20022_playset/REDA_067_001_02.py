import base_types
import RequestToPayCreditorEnrolmentAmendmentRequestV02

class REDA_067_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqToPayCdtrEnrlmntAmdmntReq"]
		@property
		def ReqToPayCdtrEnrlmntAmdmntReq(self):
			return self._ReqToPayCdtrEnrlmntAmdmntReq

		@ReqToPayCdtrEnrlmntAmdmntReq.setter
		def ReqToPayCdtrEnrlmntAmdmntReq(self, value):
			self._ReqToPayCdtrEnrlmntAmdmntReq = value if type(value) != auto else self.make_default("ReqToPayCdtrEnrlmntAmdmntReq")

		@ReqToPayCdtrEnrlmntAmdmntReq.deleter
		def ReqToPayCdtrEnrlmntAmdmntReq(self):
			del self._ReqToPayCdtrEnrlmntAmdmntReq
			self._ReqToPayCdtrEnrlmntAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayCdtrEnrlmntAmdmntReq', type=RequestToPayCreditorEnrolmentAmendmentRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

