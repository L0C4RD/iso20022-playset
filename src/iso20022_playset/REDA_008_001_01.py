from . import base_types
from .SecurityCreationStatusAdviceV01 import SecurityCreationStatusAdviceV01

class REDA_008_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyCreStsAdvc"]
		@property
		def SctyCreStsAdvc(self):
			return self._SctyCreStsAdvc

		@SctyCreStsAdvc.setter
		def SctyCreStsAdvc(self, value):
			self._SctyCreStsAdvc = value if type(value) != auto else self.make_default("SctyCreStsAdvc")

		@SctyCreStsAdvc.deleter
		def SctyCreStsAdvc(self):
			del self._SctyCreStsAdvc
			self._SctyCreStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCreStsAdvc', type=SecurityCreationStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

