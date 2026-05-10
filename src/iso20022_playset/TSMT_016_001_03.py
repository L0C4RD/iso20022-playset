from . import base_types
import ErrorReportV03

class TSMT_016_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ErrRpt"]
		@property
		def ErrRpt(self):
			return self._ErrRpt

		@ErrRpt.setter
		def ErrRpt(self, value):
			self._ErrRpt = value if type(value) != auto else self.make_default("ErrRpt")

		@ErrRpt.deleter
		def ErrRpt(self):
			del self._ErrRpt
			self._ErrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ErrRpt', type=ErrorReportV03, min=1, max=1, mutex_group=None, array=False),
		))

