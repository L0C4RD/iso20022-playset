from . import base_types
from .SecurityQueryV01 import SecurityQueryV01

class REDA_010_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyQry"]
		@property
		def SctyQry(self):
			return self._SctyQry

		@SctyQry.setter
		def SctyQry(self, value):
			self._SctyQry = value if type(value) != base_types.auto else self.make_default("SctyQry")

		@SctyQry.deleter
		def SctyQry(self):
			del self._SctyQry
			self._SctyQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyQry', type=SecurityQueryV01, min=1, max=1, mutex_group=None, array=False),
		))

