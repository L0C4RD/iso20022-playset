from . import base_types
from ._AcceptorCancellationAdviceResponseV14 import AcceptorCancellationAdviceResponseV14

class CAAA_008_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCxlAdvcRspn"]
		@property
		def AccptrCxlAdvcRspn(self):
			return self._AccptrCxlAdvcRspn

		@AccptrCxlAdvcRspn.setter
		def AccptrCxlAdvcRspn(self, value):
			self._AccptrCxlAdvcRspn = value if type(value) != base_types.auto else self.make_default("AccptrCxlAdvcRspn")

		@AccptrCxlAdvcRspn.deleter
		def AccptrCxlAdvcRspn(self):
			del self._AccptrCxlAdvcRspn
			self._AccptrCxlAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlAdvcRspn', type=AcceptorCancellationAdviceResponseV14, min=1, max=1, mutex_group=None, array=False),
		))

