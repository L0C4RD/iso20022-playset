from . import base_types
from .SecurityCSDLinkCreationRequestV01 import SecurityCSDLinkCreationRequestV01

class REDA_045_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyCSDLkCreReq"]
		@property
		def SctyCSDLkCreReq(self):
			return self._SctyCSDLkCreReq

		@SctyCSDLkCreReq.setter
		def SctyCSDLkCreReq(self, value):
			self._SctyCSDLkCreReq = value if type(value) != base_types.auto else self.make_default("SctyCSDLkCreReq")

		@SctyCSDLkCreReq.deleter
		def SctyCSDLkCreReq(self):
			del self._SctyCSDLkCreReq
			self._SctyCSDLkCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCSDLkCreReq', type=SecurityCSDLinkCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

