from . import base_types
from ._GetLimitV08 import GetLimitV08

class CAMT_009_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_GetLmt"]
		@property
		def GetLmt(self):
			return self._GetLmt

		@GetLmt.setter
		def GetLmt(self, value):
			self._GetLmt = value if type(value) != base_types.auto else self.make_default("GetLmt")

		@GetLmt.deleter
		def GetLmt(self):
			del self._GetLmt
			self._GetLmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetLmt', type=GetLimitV08, min=1, max=1, mutex_group=None, array=False),
		))

