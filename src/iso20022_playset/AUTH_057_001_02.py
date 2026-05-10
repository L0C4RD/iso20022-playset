from . import base_types
from .CCPPortfolioStressTestingDefinitionReportV02 import CCPPortfolioStressTestingDefinitionReportV02

class AUTH_057_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPPrtflStrssTstgDefRpt"]
		@property
		def CCPPrtflStrssTstgDefRpt(self):
			return self._CCPPrtflStrssTstgDefRpt

		@CCPPrtflStrssTstgDefRpt.setter
		def CCPPrtflStrssTstgDefRpt(self, value):
			self._CCPPrtflStrssTstgDefRpt = value if type(value) != base_types.auto else self.make_default("CCPPrtflStrssTstgDefRpt")

		@CCPPrtflStrssTstgDefRpt.deleter
		def CCPPrtflStrssTstgDefRpt(self):
			del self._CCPPrtflStrssTstgDefRpt
			self._CCPPrtflStrssTstgDefRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPPrtflStrssTstgDefRpt', type=CCPPortfolioStressTestingDefinitionReportV02, min=1, max=1, mutex_group=None, array=False),
		))

