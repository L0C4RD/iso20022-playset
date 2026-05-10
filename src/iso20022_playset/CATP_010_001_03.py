from . import base_types
from .ATMPINManagementRequestV03 import ATMPINManagementRequestV03

class CATP_010_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMPINMgmtReq"]
		@property
		def ATMPINMgmtReq(self):
			return self._ATMPINMgmtReq

		@ATMPINMgmtReq.setter
		def ATMPINMgmtReq(self, value):
			self._ATMPINMgmtReq = value if type(value) != base_types.auto else self.make_default("ATMPINMgmtReq")

		@ATMPINMgmtReq.deleter
		def ATMPINMgmtReq(self):
			del self._ATMPINMgmtReq
			self._ATMPINMgmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMPINMgmtReq', type=ATMPINManagementRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

