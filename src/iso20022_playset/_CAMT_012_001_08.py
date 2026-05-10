from . import base_types
from .DeleteLimitV08 import DeleteLimitV08

class CAMT_012_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DelLmt"]
		@property
		def DelLmt(self):
			return self._DelLmt

		@DelLmt.setter
		def DelLmt(self, value):
			self._DelLmt = value if type(value) != base_types.auto else self.make_default("DelLmt")

		@DelLmt.deleter
		def DelLmt(self):
			del self._DelLmt
			self._DelLmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DelLmt', type=DeleteLimitV08, min=1, max=1, mutex_group=None, array=False),
		))

