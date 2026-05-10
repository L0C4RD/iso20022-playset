from . import base_types
from .ATMWithdrawalResponseV03 import ATMWithdrawalResponseV03

class CATP_002_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMWdrwlRspn"]
		@property
		def ATMWdrwlRspn(self):
			return self._ATMWdrwlRspn

		@ATMWdrwlRspn.setter
		def ATMWdrwlRspn(self, value):
			self._ATMWdrwlRspn = value if type(value) != base_types.auto else self.make_default("ATMWdrwlRspn")

		@ATMWdrwlRspn.deleter
		def ATMWdrwlRspn(self):
			del self._ATMWdrwlRspn
			self._ATMWdrwlRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlRspn', type=ATMWithdrawalResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

