import base_types
import InterestPaymentRequestV05

class COLR_013_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntrstPmtReq"]
		@property
		def IntrstPmtReq(self):
			return self._IntrstPmtReq

		@IntrstPmtReq.setter
		def IntrstPmtReq(self, value):
			self._IntrstPmtReq = value if type(value) != auto else self.make_default("IntrstPmtReq")

		@IntrstPmtReq.deleter
		def IntrstPmtReq(self):
			del self._IntrstPmtReq
			self._IntrstPmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntrstPmtReq', type=InterestPaymentRequestV05, min=1, max=1, mutex_group=None, array=False),
		))

