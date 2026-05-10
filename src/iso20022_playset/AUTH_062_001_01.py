from . import base_types
from .CCPLiquidityStressTestingDefinitionReportV01 import CCPLiquidityStressTestingDefinitionReportV01

class AUTH_062_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPLqdtyStrssTstgDefRpt"]
		@property
		def CCPLqdtyStrssTstgDefRpt(self):
			return self._CCPLqdtyStrssTstgDefRpt

		@CCPLqdtyStrssTstgDefRpt.setter
		def CCPLqdtyStrssTstgDefRpt(self, value):
			self._CCPLqdtyStrssTstgDefRpt = value if type(value) != base_types.auto else self.make_default("CCPLqdtyStrssTstgDefRpt")

		@CCPLqdtyStrssTstgDefRpt.deleter
		def CCPLqdtyStrssTstgDefRpt(self):
			del self._CCPLqdtyStrssTstgDefRpt
			self._CCPLqdtyStrssTstgDefRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPLqdtyStrssTstgDefRpt', type=CCPLiquidityStressTestingDefinitionReportV01, min=1, max=1, mutex_group=None, array=False),
		))

