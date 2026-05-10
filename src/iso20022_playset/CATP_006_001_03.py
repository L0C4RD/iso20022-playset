import base_types
import ATMInquiryRequestV03

class CATP_006_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMNqryReq"]
		@property
		def ATMNqryReq(self):
			return self._ATMNqryReq

		@ATMNqryReq.setter
		def ATMNqryReq(self, value):
			self._ATMNqryReq = value if type(value) != auto else self.make_default("ATMNqryReq")

		@ATMNqryReq.deleter
		def ATMNqryReq(self):
			del self._ATMNqryReq
			self._ATMNqryReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMNqryReq', type=ATMInquiryRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

