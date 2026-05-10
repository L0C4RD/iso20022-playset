from . import base_types
from .ActionReminderV03 import ActionReminderV03

class TSMT_024_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ActnRmndr"]
		@property
		def ActnRmndr(self):
			return self._ActnRmndr

		@ActnRmndr.setter
		def ActnRmndr(self, value):
			self._ActnRmndr = value if type(value) != base_types.auto else self.make_default("ActnRmndr")

		@ActnRmndr.deleter
		def ActnRmndr(self):
			del self._ActnRmndr
			self._ActnRmndr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ActnRmndr', type=ActionReminderV03, min=1, max=1, mutex_group=None, array=False),
		))

