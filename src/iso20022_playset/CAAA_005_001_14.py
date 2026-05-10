import base_types
import AcceptorCancellationRequestV14

class CAAA_005_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCxlReq"]
		@property
		def AccptrCxlReq(self):
			return self._AccptrCxlReq

		@AccptrCxlReq.setter
		def AccptrCxlReq(self, value):
			self._AccptrCxlReq = value if type(value) != auto else self.make_default("AccptrCxlReq")

		@AccptrCxlReq.deleter
		def AccptrCxlReq(self):
			del self._AccptrCxlReq
			self._AccptrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlReq', type=AcceptorCancellationRequestV14, min=1, max=1, mutex_group=None, array=False),
		))

