from . import base_types
from ._CloseLinkDeletionRequestV01 import CloseLinkDeletionRequestV01

class REDA_077_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ClsLkDeltnReq"]
		@property
		def ClsLkDeltnReq(self):
			return self._ClsLkDeltnReq

		@ClsLkDeltnReq.setter
		def ClsLkDeltnReq(self, value):
			self._ClsLkDeltnReq = value if type(value) != base_types.auto else self.make_default("ClsLkDeltnReq")

		@ClsLkDeltnReq.deleter
		def ClsLkDeltnReq(self):
			del self._ClsLkDeltnReq
			self._ClsLkDeltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ClsLkDeltnReq', type=CloseLinkDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

