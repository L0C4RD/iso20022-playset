from . import base_types
from ._ATMWithdrawalRequestV03 import ATMWithdrawalRequestV03

class CATP_001_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMWdrwlReq"]
		@property
		def ATMWdrwlReq(self):
			return self._ATMWdrwlReq

		@ATMWdrwlReq.setter
		def ATMWdrwlReq(self, value):
			self._ATMWdrwlReq = value if type(value) != base_types.auto else self.make_default("ATMWdrwlReq")

		@ATMWdrwlReq.deleter
		def ATMWdrwlReq(self):
			del self._ATMWdrwlReq
			self._ATMWdrwlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlReq', type=ATMWithdrawalRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

