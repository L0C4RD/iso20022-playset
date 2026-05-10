import base_types
import AccountRequestAcknowledgementV04

class ACMT_010_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctReqAck"]
		@property
		def AcctReqAck(self):
			return self._AcctReqAck

		@AcctReqAck.setter
		def AcctReqAck(self, value):
			self._AcctReqAck = value if type(value) != auto else self.make_default("AcctReqAck")

		@AcctReqAck.deleter
		def AcctReqAck(self):
			del self._AcctReqAck
			self._AcctReqAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctReqAck', type=AccountRequestAcknowledgementV04, min=1, max=1, mutex_group=None, array=False),
		))

