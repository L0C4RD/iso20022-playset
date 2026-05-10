import base_types
import NotificationOfCaseAssignmentV06

class CAMT_030_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NtfctnOfCaseAssgnmt"]
		@property
		def NtfctnOfCaseAssgnmt(self):
			return self._NtfctnOfCaseAssgnmt

		@NtfctnOfCaseAssgnmt.setter
		def NtfctnOfCaseAssgnmt(self, value):
			self._NtfctnOfCaseAssgnmt = value if type(value) != auto else self.make_default("NtfctnOfCaseAssgnmt")

		@NtfctnOfCaseAssgnmt.deleter
		def NtfctnOfCaseAssgnmt(self):
			del self._NtfctnOfCaseAssgnmt
			self._NtfctnOfCaseAssgnmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnOfCaseAssgnmt', type=NotificationOfCaseAssignmentV06, min=1, max=1, mutex_group=None, array=False),
		))

