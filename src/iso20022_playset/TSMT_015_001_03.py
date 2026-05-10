from . import base_types
from .DeltaReportV03 import DeltaReportV03

class TSMT_015_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DltaRpt"]
		@property
		def DltaRpt(self):
			return self._DltaRpt

		@DltaRpt.setter
		def DltaRpt(self, value):
			self._DltaRpt = value if type(value) != auto else self.make_default("DltaRpt")

		@DltaRpt.deleter
		def DltaRpt(self):
			del self._DltaRpt
			self._DltaRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DltaRpt', type=DeltaReportV03, min=1, max=1, mutex_group=None, array=False),
		))

