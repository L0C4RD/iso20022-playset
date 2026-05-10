from . import base_types
from ._ATMPINManagementResponseV03 import ATMPINManagementResponseV03

class CATP_011_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMPINMgmtRspn"]
		@property
		def ATMPINMgmtRspn(self):
			return self._ATMPINMgmtRspn

		@ATMPINMgmtRspn.setter
		def ATMPINMgmtRspn(self, value):
			self._ATMPINMgmtRspn = value if type(value) != base_types.auto else self.make_default("ATMPINMgmtRspn")

		@ATMPINMgmtRspn.deleter
		def ATMPINMgmtRspn(self):
			del self._ATMPINMgmtRspn
			self._ATMPINMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMPINMgmtRspn', type=ATMPINManagementResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

