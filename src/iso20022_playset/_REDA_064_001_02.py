from . import base_types
from ._CalendarQueryV02 import CalendarQueryV02

class REDA_064_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CalQry"]
		@property
		def CalQry(self):
			return self._CalQry

		@CalQry.setter
		def CalQry(self, value):
			self._CalQry = value if type(value) != base_types.auto else self.make_default("CalQry")

		@CalQry.deleter
		def CalQry(self):
			del self._CalQry
			self._CalQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CalQry', type=CalendarQueryV02, min=1, max=1, mutex_group=None, array=False),
		))

