from . import base_types
from ._CCPMemberRequirementsReportV01 import CCPMemberRequirementsReportV01

class AUTH_055_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPMmbRqrmntsRpt"]
		@property
		def CCPMmbRqrmntsRpt(self):
			return self._CCPMmbRqrmntsRpt

		@CCPMmbRqrmntsRpt.setter
		def CCPMmbRqrmntsRpt(self, value):
			self._CCPMmbRqrmntsRpt = value if type(value) != base_types.auto else self.make_default("CCPMmbRqrmntsRpt")

		@CCPMmbRqrmntsRpt.deleter
		def CCPMmbRqrmntsRpt(self):
			del self._CCPMmbRqrmntsRpt
			self._CCPMmbRqrmntsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPMmbRqrmntsRpt', type=CCPMemberRequirementsReportV01, min=1, max=1, mutex_group=None, array=False),
		))

