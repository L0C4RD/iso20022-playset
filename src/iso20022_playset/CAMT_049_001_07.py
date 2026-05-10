from . import base_types
from .DeleteReservationV07 import DeleteReservationV07

class CAMT_049_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DelRsvatn"]
		@property
		def DelRsvatn(self):
			return self._DelRsvatn

		@DelRsvatn.setter
		def DelRsvatn(self, value):
			self._DelRsvatn = value if type(value) != base_types.auto else self.make_default("DelRsvatn")

		@DelRsvatn.deleter
		def DelRsvatn(self):
			del self._DelRsvatn
			self._DelRsvatn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DelRsvatn', type=DeleteReservationV07, min=1, max=1, mutex_group=None, array=False),
		))

