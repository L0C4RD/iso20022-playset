from . import base_types
from .SecurityDeletionStatusAdviceV01 import SecurityDeletionStatusAdviceV01

class REDA_030_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyDeltnStsAdvc"]
		@property
		def SctyDeltnStsAdvc(self):
			return self._SctyDeltnStsAdvc

		@SctyDeltnStsAdvc.setter
		def SctyDeltnStsAdvc(self, value):
			self._SctyDeltnStsAdvc = value if type(value) != base_types.auto else self.make_default("SctyDeltnStsAdvc")

		@SctyDeltnStsAdvc.deleter
		def SctyDeltnStsAdvc(self):
			del self._SctyDeltnStsAdvc
			self._SctyDeltnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyDeltnStsAdvc', type=SecurityDeletionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

