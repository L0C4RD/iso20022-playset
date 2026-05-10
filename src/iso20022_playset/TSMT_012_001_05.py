from . import base_types
from .BaselineReSubmissionV05 import BaselineReSubmissionV05

class TSMT_012_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BaselnReSubmissn"]
		@property
		def BaselnReSubmissn(self):
			return self._BaselnReSubmissn

		@BaselnReSubmissn.setter
		def BaselnReSubmissn(self, value):
			self._BaselnReSubmissn = value if type(value) != auto else self.make_default("BaselnReSubmissn")

		@BaselnReSubmissn.deleter
		def BaselnReSubmissn(self):
			del self._BaselnReSubmissn
			self._BaselnReSubmissn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BaselnReSubmissn', type=BaselineReSubmissionV05, min=1, max=1, mutex_group=None, array=False),
		))

