from . import base_types
from ._FileActionResponseV04 import FileActionResponseV04

class CAFM_002_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FileActnRspn"]
		@property
		def FileActnRspn(self):
			return self._FileActnRspn

		@FileActnRspn.setter
		def FileActnRspn(self, value):
			self._FileActnRspn = value if type(value) != base_types.auto else self.make_default("FileActnRspn")

		@FileActnRspn.deleter
		def FileActnRspn(self):
			del self._FileActnRspn
			self._FileActnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FileActnRspn', type=FileActionResponseV04, min=1, max=1, mutex_group=None, array=False),
		))

