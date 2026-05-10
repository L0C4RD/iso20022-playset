from . import base_types
from ._CCPInteroperabilityReportV01 import CCPInteroperabilityReportV01

class AUTH_112_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPIntrprbltyRpt"]
		@property
		def CCPIntrprbltyRpt(self):
			return self._CCPIntrprbltyRpt

		@CCPIntrprbltyRpt.setter
		def CCPIntrprbltyRpt(self, value):
			self._CCPIntrprbltyRpt = value if type(value) != base_types.auto else self.make_default("CCPIntrprbltyRpt")

		@CCPIntrprbltyRpt.deleter
		def CCPIntrprbltyRpt(self):
			del self._CCPIntrprbltyRpt
			self._CCPIntrprbltyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPIntrprbltyRpt', type=CCPInteroperabilityReportV01, min=1, max=1, mutex_group=None, array=False),
		))

