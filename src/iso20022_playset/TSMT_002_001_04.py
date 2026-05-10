from . import base_types
from .ActivityReportV04 import ActivityReportV04

class TSMT_002_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ActvtyRpt"]
		@property
		def ActvtyRpt(self):
			return self._ActvtyRpt

		@ActvtyRpt.setter
		def ActvtyRpt(self, value):
			self._ActvtyRpt = value if type(value) != base_types.auto else self.make_default("ActvtyRpt")

		@ActvtyRpt.deleter
		def ActvtyRpt(self):
			del self._ActvtyRpt
			self._ActvtyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ActvtyRpt', type=ActivityReportV04, min=1, max=1, mutex_group=None, array=False),
		))

