from . import base_types
from .CancelCaseAssignmentV05 import CancelCaseAssignmentV05

class CAMT_032_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CclCaseAssgnmt"]
		@property
		def CclCaseAssgnmt(self):
			return self._CclCaseAssgnmt

		@CclCaseAssgnmt.setter
		def CclCaseAssgnmt(self, value):
			self._CclCaseAssgnmt = value if type(value) != base_types.auto else self.make_default("CclCaseAssgnmt")

		@CclCaseAssgnmt.deleter
		def CclCaseAssgnmt(self):
			del self._CclCaseAssgnmt
			self._CclCaseAssgnmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CclCaseAssgnmt', type=CancelCaseAssignmentV05, min=1, max=1, mutex_group=None, array=False),
		))

