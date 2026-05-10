from . import base_types
from .ErrorV04 import ErrorV04

class CAAD_007_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_Err"]
		@property
		def Err(self):
			return self._Err

		@Err.setter
		def Err(self, value):
			self._Err = value if type(value) != auto else self.make_default("Err")

		@Err.deleter
		def Err(self):
			del self._Err
			self._Err = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='Err', type=ErrorV04, min=1, max=1, mutex_group=None, array=False),
		))

