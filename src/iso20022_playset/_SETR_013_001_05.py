from . import base_types
from ._SwitchOrderV05 import SwitchOrderV05

class SETR_013_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SwtchOrdr"]
		@property
		def SwtchOrdr(self):
			return self._SwtchOrdr

		@SwtchOrdr.setter
		def SwtchOrdr(self, value):
			self._SwtchOrdr = value if type(value) != base_types.auto else self.make_default("SwtchOrdr")

		@SwtchOrdr.deleter
		def SwtchOrdr(self):
			del self._SwtchOrdr
			self._SwtchOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdr', type=SwitchOrderV05, min=1, max=1, mutex_group=None, array=False),
		))

