from . import base_types
from .ATMWithdrawalCompletionAcknowledgementV03 import ATMWithdrawalCompletionAcknowledgementV03

class CATP_004_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMWdrwlCmpltnAck"]
		@property
		def ATMWdrwlCmpltnAck(self):
			return self._ATMWdrwlCmpltnAck

		@ATMWdrwlCmpltnAck.setter
		def ATMWdrwlCmpltnAck(self, value):
			self._ATMWdrwlCmpltnAck = value if type(value) != auto else self.make_default("ATMWdrwlCmpltnAck")

		@ATMWdrwlCmpltnAck.deleter
		def ATMWdrwlCmpltnAck(self):
			del self._ATMWdrwlCmpltnAck
			self._ATMWdrwlCmpltnAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlCmpltnAck', type=ATMWithdrawalCompletionAcknowledgementV03, min=1, max=1, mutex_group=None, array=False),
		))

