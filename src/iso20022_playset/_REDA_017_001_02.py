from . import base_types
from ._PartyReportV02 import PartyReportV02

class REDA_017_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyRpt"]
		@property
		def PtyRpt(self):
			return self._PtyRpt

		@PtyRpt.setter
		def PtyRpt(self, value):
			self._PtyRpt = value if type(value) != base_types.auto else self.make_default("PtyRpt")

		@PtyRpt.deleter
		def PtyRpt(self):
			del self._PtyRpt
			self._PtyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRpt', type=PartyReportV02, min=1, max=1, mutex_group=None, array=False),
		))

