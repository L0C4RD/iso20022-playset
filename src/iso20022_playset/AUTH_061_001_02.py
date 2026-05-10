import base_types
import CCPInvestmentsReportV02

class AUTH_061_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPInvstmtsRpt"]
		@property
		def CCPInvstmtsRpt(self):
			return self._CCPInvstmtsRpt

		@CCPInvstmtsRpt.setter
		def CCPInvstmtsRpt(self, value):
			self._CCPInvstmtsRpt = value if type(value) != auto else self.make_default("CCPInvstmtsRpt")

		@CCPInvstmtsRpt.deleter
		def CCPInvstmtsRpt(self):
			del self._CCPInvstmtsRpt
			self._CCPInvstmtsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPInvstmtsRpt', type=CCPInvestmentsReportV02, min=1, max=1, mutex_group=None, array=False),
		))

