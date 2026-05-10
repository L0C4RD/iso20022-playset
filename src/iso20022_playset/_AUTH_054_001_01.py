from . import base_types
from .CCPClearingMemberReportV01 import CCPClearingMemberReportV01

class AUTH_054_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPClrMmbRpt"]
		@property
		def CCPClrMmbRpt(self):
			return self._CCPClrMmbRpt

		@CCPClrMmbRpt.setter
		def CCPClrMmbRpt(self, value):
			self._CCPClrMmbRpt = value if type(value) != base_types.auto else self.make_default("CCPClrMmbRpt")

		@CCPClrMmbRpt.deleter
		def CCPClrMmbRpt(self):
			del self._CCPClrMmbRpt
			self._CCPClrMmbRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPClrMmbRpt', type=CCPClearingMemberReportV01, min=1, max=1, mutex_group=None, array=False),
		))

