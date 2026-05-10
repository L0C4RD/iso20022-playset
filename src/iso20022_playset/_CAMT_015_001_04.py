from . import base_types
from .ModifyMemberV04 import ModifyMemberV04

class CAMT_015_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ModfyMmb"]
		@property
		def ModfyMmb(self):
			return self._ModfyMmb

		@ModfyMmb.setter
		def ModfyMmb(self, value):
			self._ModfyMmb = value if type(value) != base_types.auto else self.make_default("ModfyMmb")

		@ModfyMmb.deleter
		def ModfyMmb(self):
			del self._ModfyMmb
			self._ModfyMmb = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyMmb', type=ModifyMemberV04, min=1, max=1, mutex_group=None, array=False),
		))

