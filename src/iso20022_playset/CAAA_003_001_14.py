from . import base_types
from .AcceptorCompletionAdviceV14 import AcceptorCompletionAdviceV14

class CAAA_003_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCmpltnAdvc"]
		@property
		def AccptrCmpltnAdvc(self):
			return self._AccptrCmpltnAdvc

		@AccptrCmpltnAdvc.setter
		def AccptrCmpltnAdvc(self, value):
			self._AccptrCmpltnAdvc = value if type(value) != base_types.auto else self.make_default("AccptrCmpltnAdvc")

		@AccptrCmpltnAdvc.deleter
		def AccptrCmpltnAdvc(self):
			del self._AccptrCmpltnAdvc
			self._AccptrCmpltnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCmpltnAdvc', type=AcceptorCompletionAdviceV14, min=1, max=1, mutex_group=None, array=False),
		))

