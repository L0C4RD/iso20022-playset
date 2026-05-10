from . import base_types
import AcceptorCancellationAdviceV14

class CAAA_007_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCxlAdvc"]
		@property
		def AccptrCxlAdvc(self):
			return self._AccptrCxlAdvc

		@AccptrCxlAdvc.setter
		def AccptrCxlAdvc(self, value):
			self._AccptrCxlAdvc = value if type(value) != auto else self.make_default("AccptrCxlAdvc")

		@AccptrCxlAdvc.deleter
		def AccptrCxlAdvc(self):
			del self._AccptrCxlAdvc
			self._AccptrCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlAdvc', type=AcceptorCancellationAdviceV14, min=1, max=1, mutex_group=None, array=False),
		))

