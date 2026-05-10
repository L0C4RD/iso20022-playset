from . import base_types
from .GetMemberV04 import GetMemberV04

class CAMT_013_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_GetMmb"]
		@property
		def GetMmb(self):
			return self._GetMmb

		@GetMmb.setter
		def GetMmb(self, value):
			self._GetMmb = value if type(value) != auto else self.make_default("GetMmb")

		@GetMmb.deleter
		def GetMmb(self):
			del self._GetMmb
			self._GetMmb = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetMmb', type=GetMemberV04, min=1, max=1, mutex_group=None, array=False),
		))

