from . import base_types
from .AcceptorAuthorisationResponseV14 import AcceptorAuthorisationResponseV14

class CAAA_002_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrAuthstnRspn"]
		@property
		def AccptrAuthstnRspn(self):
			return self._AccptrAuthstnRspn

		@AccptrAuthstnRspn.setter
		def AccptrAuthstnRspn(self, value):
			self._AccptrAuthstnRspn = value if type(value) != base_types.auto else self.make_default("AccptrAuthstnRspn")

		@AccptrAuthstnRspn.deleter
		def AccptrAuthstnRspn(self):
			del self._AccptrAuthstnRspn
			self._AccptrAuthstnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrAuthstnRspn', type=AcceptorAuthorisationResponseV14, min=1, max=1, mutex_group=None, array=False),
		))

