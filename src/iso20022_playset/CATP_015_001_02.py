from . import base_types
from .ATMDepositCompletionAcknowledgementV02 import ATMDepositCompletionAcknowledgementV02

class CATP_015_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMDpstCmpltnAck"]
		@property
		def ATMDpstCmpltnAck(self):
			return self._ATMDpstCmpltnAck

		@ATMDpstCmpltnAck.setter
		def ATMDpstCmpltnAck(self, value):
			self._ATMDpstCmpltnAck = value if type(value) != auto else self.make_default("ATMDpstCmpltnAck")

		@ATMDpstCmpltnAck.deleter
		def ATMDpstCmpltnAck(self):
			del self._ATMDpstCmpltnAck
			self._ATMDpstCmpltnAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDpstCmpltnAck', type=ATMDepositCompletionAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))

