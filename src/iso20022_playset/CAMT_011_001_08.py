from . import base_types
from .ModifyLimitV08 import ModifyLimitV08

class CAMT_011_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ModfyLmt"]
		@property
		def ModfyLmt(self):
			return self._ModfyLmt

		@ModfyLmt.setter
		def ModfyLmt(self, value):
			self._ModfyLmt = value if type(value) != base_types.auto else self.make_default("ModfyLmt")

		@ModfyLmt.deleter
		def ModfyLmt(self):
			del self._ModfyLmt
			self._ModfyLmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyLmt', type=ModifyLimitV08, min=1, max=1, mutex_group=None, array=False),
		))

