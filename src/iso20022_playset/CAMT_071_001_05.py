import base_types
import DeleteStandingOrderV05

class CAMT_071_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DelStgOrdr"]
		@property
		def DelStgOrdr(self):
			return self._DelStgOrdr

		@DelStgOrdr.setter
		def DelStgOrdr(self, value):
			self._DelStgOrdr = value if type(value) != auto else self.make_default("DelStgOrdr")

		@DelStgOrdr.deleter
		def DelStgOrdr(self):
			del self._DelStgOrdr
			self._DelStgOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DelStgOrdr', type=DeleteStandingOrderV05, min=1, max=1, mutex_group=None, array=False),
		))

