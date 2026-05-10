from . import base_types
from .ATMCompletionAcknowledgementV03 import ATMCompletionAcknowledgementV03

class CATP_009_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMCmpltnAck"]
		@property
		def ATMCmpltnAck(self):
			return self._ATMCmpltnAck

		@ATMCmpltnAck.setter
		def ATMCmpltnAck(self, value):
			self._ATMCmpltnAck = value if type(value) != auto else self.make_default("ATMCmpltnAck")

		@ATMCmpltnAck.deleter
		def ATMCmpltnAck(self):
			del self._ATMCmpltnAck
			self._ATMCmpltnAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMCmpltnAck', type=ATMCompletionAcknowledgementV03, min=1, max=1, mutex_group=None, array=False),
		))

