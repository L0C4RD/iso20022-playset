from . import base_types
from .SecurityActivityAdviceV01 import SecurityActivityAdviceV01

class REDA_009_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyActvtyAdvc"]
		@property
		def SctyActvtyAdvc(self):
			return self._SctyActvtyAdvc

		@SctyActvtyAdvc.setter
		def SctyActvtyAdvc(self, value):
			self._SctyActvtyAdvc = value if type(value) != base_types.auto else self.make_default("SctyActvtyAdvc")

		@SctyActvtyAdvc.deleter
		def SctyActvtyAdvc(self):
			del self._SctyActvtyAdvc
			self._SctyActvtyAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyActvtyAdvc', type=SecurityActivityAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

