from . import base_types
from ._PartyCreationRequestV02 import PartyCreationRequestV02

class REDA_014_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyCreReq"]
		@property
		def PtyCreReq(self):
			return self._PtyCreReq

		@PtyCreReq.setter
		def PtyCreReq(self, value):
			self._PtyCreReq = value if type(value) != base_types.auto else self.make_default("PtyCreReq")

		@PtyCreReq.deleter
		def PtyCreReq(self):
			del self._PtyCreReq
			self._PtyCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyCreReq', type=PartyCreationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

