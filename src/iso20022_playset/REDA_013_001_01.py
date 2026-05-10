from . import base_types
from .SecurityDeletionRequestV01 import SecurityDeletionRequestV01

class REDA_013_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyDeltnReq"]
		@property
		def SctyDeltnReq(self):
			return self._SctyDeltnReq

		@SctyDeltnReq.setter
		def SctyDeltnReq(self, value):
			self._SctyDeltnReq = value if type(value) != auto else self.make_default("SctyDeltnReq")

		@SctyDeltnReq.deleter
		def SctyDeltnReq(self):
			del self._SctyDeltnReq
			self._SctyDeltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyDeltnReq', type=SecurityDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

