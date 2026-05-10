from . import base_types
from .FileActionInitiationV03 import FileActionInitiationV03

class CAFM_001_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FileActnInitn"]
		@property
		def FileActnInitn(self):
			return self._FileActnInitn

		@FileActnInitn.setter
		def FileActnInitn(self, value):
			self._FileActnInitn = value if type(value) != auto else self.make_default("FileActnInitn")

		@FileActnInitn.deleter
		def FileActnInitn(self):
			del self._FileActnInitn
			self._FileActnInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FileActnInitn', type=FileActionInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))

