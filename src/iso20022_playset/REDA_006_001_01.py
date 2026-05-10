from . import base_types
from .SecurityCreationRequestV01 import SecurityCreationRequestV01

class REDA_006_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyCreReq"]
		@property
		def SctyCreReq(self):
			return self._SctyCreReq

		@SctyCreReq.setter
		def SctyCreReq(self, value):
			self._SctyCreReq = value if type(value) != auto else self.make_default("SctyCreReq")

		@SctyCreReq.deleter
		def SctyCreReq(self):
			del self._SctyCreReq
			self._SctyCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCreReq', type=SecurityCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

