import base_types
import ATMInquiryResponseV03

class CATP_007_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMNqryRspn"]
		@property
		def ATMNqryRspn(self):
			return self._ATMNqryRspn

		@ATMNqryRspn.setter
		def ATMNqryRspn(self, value):
			self._ATMNqryRspn = value if type(value) != auto else self.make_default("ATMNqryRspn")

		@ATMNqryRspn.deleter
		def ATMNqryRspn(self):
			del self._ATMNqryRspn
			self._ATMNqryRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMNqryRspn', type=ATMInquiryResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

