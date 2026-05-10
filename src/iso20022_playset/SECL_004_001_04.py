import base_types
import NetPositionV04

class SECL_004_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NetPos"]
		@property
		def NetPos(self):
			return self._NetPos

		@NetPos.setter
		def NetPos(self, value):
			self._NetPos = value if type(value) != auto else self.make_default("NetPos")

		@NetPos.deleter
		def NetPos(self):
			del self._NetPos
			self._NetPos = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NetPos', type=NetPositionV04, min=1, max=1, mutex_group=None, array=False),
		))

