from . import base_types
import UnableToApplyV10

class CAMT_026_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UblToApply"]
		@property
		def UblToApply(self):
			return self._UblToApply

		@UblToApply.setter
		def UblToApply(self, value):
			self._UblToApply = value if type(value) != auto else self.make_default("UblToApply")

		@UblToApply.deleter
		def UblToApply(self):
			del self._UblToApply
			self._UblToApply = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UblToApply', type=UnableToApplyV10, min=1, max=1, mutex_group=None, array=False),
		))

