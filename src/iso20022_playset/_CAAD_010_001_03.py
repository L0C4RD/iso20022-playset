from . import base_types
from ._CustomReportV03 import CustomReportV03

class CAAD_010_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CstmRpt"]
		@property
		def CstmRpt(self):
			return self._CstmRpt

		@CstmRpt.setter
		def CstmRpt(self, value):
			self._CstmRpt = value if type(value) != base_types.auto else self.make_default("CstmRpt")

		@CstmRpt.deleter
		def CstmRpt(self):
			del self._CstmRpt
			self._CstmRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmRpt', type=CustomReportV03, min=1, max=1, mutex_group=None, array=False),
		))

