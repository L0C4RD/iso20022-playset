import base_types
import MeetingCancellationV10

class SEEV_002_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MtgCxl"]
		@property
		def MtgCxl(self):
			return self._MtgCxl

		@MtgCxl.setter
		def MtgCxl(self, value):
			self._MtgCxl = value if type(value) != auto else self.make_default("MtgCxl")

		@MtgCxl.deleter
		def MtgCxl(self):
			del self._MtgCxl
			self._MtgCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgCxl', type=MeetingCancellationV10, min=1, max=1, mutex_group=None, array=False),
		))

