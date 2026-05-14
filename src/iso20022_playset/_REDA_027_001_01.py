from . import base_types
from ._CloseLinkCreationRequestV01 import CloseLinkCreationRequestV01

class REDA_027_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ClsLkCreReq"]
		@property
		def ClsLkCreReq(self):
			return self._ClsLkCreReq

		@ClsLkCreReq.setter
		def ClsLkCreReq(self, value):
			self._ClsLkCreReq = value if type(value) != base_types.auto else self.make_default("ClsLkCreReq")

		@ClsLkCreReq.deleter
		def ClsLkCreReq(self):
			del self._ClsLkCreReq
			self._ClsLkCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ClsLkCreReq', type=CloseLinkCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

