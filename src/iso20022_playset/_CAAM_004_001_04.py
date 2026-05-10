from . import base_types
from .ATMKeyDownloadResponseV04 import ATMKeyDownloadResponseV04

class CAAM_004_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMKeyDwnldRspn"]
		@property
		def ATMKeyDwnldRspn(self):
			return self._ATMKeyDwnldRspn

		@ATMKeyDwnldRspn.setter
		def ATMKeyDwnldRspn(self, value):
			self._ATMKeyDwnldRspn = value if type(value) != base_types.auto else self.make_default("ATMKeyDwnldRspn")

		@ATMKeyDwnldRspn.deleter
		def ATMKeyDwnldRspn(self):
			del self._ATMKeyDwnldRspn
			self._ATMKeyDwnldRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMKeyDwnldRspn', type=ATMKeyDownloadResponseV04, min=1, max=1, mutex_group=None, array=False),
		))

