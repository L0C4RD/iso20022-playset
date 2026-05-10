from . import base_types
from .AcceptorCancellationResponseV13 import AcceptorCancellationResponseV13

class CAAA_006_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCxlRspn"]
		@property
		def AccptrCxlRspn(self):
			return self._AccptrCxlRspn

		@AccptrCxlRspn.setter
		def AccptrCxlRspn(self, value):
			self._AccptrCxlRspn = value if type(value) != auto else self.make_default("AccptrCxlRspn")

		@AccptrCxlRspn.deleter
		def AccptrCxlRspn(self):
			del self._AccptrCxlRspn
			self._AccptrCxlRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlRspn', type=AcceptorCancellationResponseV13, min=1, max=1, mutex_group=None, array=False),
		))

