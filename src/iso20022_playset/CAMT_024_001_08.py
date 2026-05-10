from . import base_types
from .ModifyStandingOrderV08 import ModifyStandingOrderV08

class CAMT_024_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ModfyStgOrdr"]
		@property
		def ModfyStgOrdr(self):
			return self._ModfyStgOrdr

		@ModfyStgOrdr.setter
		def ModfyStgOrdr(self, value):
			self._ModfyStgOrdr = value if type(value) != auto else self.make_default("ModfyStgOrdr")

		@ModfyStgOrdr.deleter
		def ModfyStgOrdr(self):
			del self._ModfyStgOrdr
			self._ModfyStgOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyStgOrdr', type=ModifyStandingOrderV08, min=1, max=1, mutex_group=None, array=False),
		))

