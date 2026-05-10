from . import base_types
from .InitialBaselineSubmissionV05 import InitialBaselineSubmissionV05

class TSMT_019_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InitlBaselnSubmissn"]
		@property
		def InitlBaselnSubmissn(self):
			return self._InitlBaselnSubmissn

		@InitlBaselnSubmissn.setter
		def InitlBaselnSubmissn(self, value):
			self._InitlBaselnSubmissn = value if type(value) != base_types.auto else self.make_default("InitlBaselnSubmissn")

		@InitlBaselnSubmissn.deleter
		def InitlBaselnSubmissn(self):
			del self._InitlBaselnSubmissn
			self._InitlBaselnSubmissn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InitlBaselnSubmissn', type=InitialBaselineSubmissionV05, min=1, max=1, mutex_group=None, array=False),
		))

