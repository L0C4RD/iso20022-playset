import base_types
import AccountLinkCreationRequestV01

class REDA_049_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctLkCreReq"]
		@property
		def AcctLkCreReq(self):
			return self._AcctLkCreReq

		@AcctLkCreReq.setter
		def AcctLkCreReq(self, value):
			self._AcctLkCreReq = value if type(value) != auto else self.make_default("AcctLkCreReq")

		@AcctLkCreReq.deleter
		def AcctLkCreReq(self):
			del self._AcctLkCreReq
			self._AcctLkCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctLkCreReq', type=AccountLinkCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

