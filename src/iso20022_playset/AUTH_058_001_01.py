import base_types
import CCPPortfolioStressTestingResultReportV01

class AUTH_058_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPPrtflStrssTstgRsltRpt"]
		@property
		def CCPPrtflStrssTstgRsltRpt(self):
			return self._CCPPrtflStrssTstgRsltRpt

		@CCPPrtflStrssTstgRsltRpt.setter
		def CCPPrtflStrssTstgRsltRpt(self, value):
			self._CCPPrtflStrssTstgRsltRpt = value if type(value) != auto else self.make_default("CCPPrtflStrssTstgRsltRpt")

		@CCPPrtflStrssTstgRsltRpt.deleter
		def CCPPrtflStrssTstgRsltRpt(self):
			del self._CCPPrtflStrssTstgRsltRpt
			self._CCPPrtflStrssTstgRsltRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPPrtflStrssTstgRsltRpt', type=CCPPortfolioStressTestingResultReportV01, min=1, max=1, mutex_group=None, array=False),
		))

