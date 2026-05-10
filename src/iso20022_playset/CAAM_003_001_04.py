from . import base_types
from .ATMKeyDownloadRequestV04 import ATMKeyDownloadRequestV04

class CAAM_003_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMKeyDwnldReq"]
		@property
		def ATMKeyDwnldReq(self):
			return self._ATMKeyDwnldReq

		@ATMKeyDwnldReq.setter
		def ATMKeyDwnldReq(self, value):
			self._ATMKeyDwnldReq = value if type(value) != auto else self.make_default("ATMKeyDwnldReq")

		@ATMKeyDwnldReq.deleter
		def ATMKeyDwnldReq(self):
			del self._ATMKeyDwnldReq
			self._ATMKeyDwnldReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMKeyDwnldReq', type=ATMKeyDownloadRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

