from . import base_types
from ._CreateStandingOrderV03 import CreateStandingOrderV03

class CAMT_102_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CretStgOrdr"]
		@property
		def CretStgOrdr(self):
			return self._CretStgOrdr

		@CretStgOrdr.setter
		def CretStgOrdr(self, value):
			self._CretStgOrdr = value if type(value) != base_types.auto else self.make_default("CretStgOrdr")

		@CretStgOrdr.deleter
		def CretStgOrdr(self):
			del self._CretStgOrdr
			self._CretStgOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CretStgOrdr', type=CreateStandingOrderV03, min=1, max=1, mutex_group=None, array=False),
		))

