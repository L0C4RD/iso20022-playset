from . import base_types
import PartyDeletionRequestV01

class REDA_031_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyDeltnReq"]
		@property
		def PtyDeltnReq(self):
			return self._PtyDeltnReq

		@PtyDeltnReq.setter
		def PtyDeltnReq(self, value):
			self._PtyDeltnReq = value if type(value) != auto else self.make_default("PtyDeltnReq")

		@PtyDeltnReq.deleter
		def PtyDeltnReq(self):
			del self._PtyDeltnReq
			self._PtyDeltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyDeltnReq', type=PartyDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

