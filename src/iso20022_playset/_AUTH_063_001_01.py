# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPLiquidityStressTestingResultReportV01 import CCPLiquidityStressTestingResultReportV01

class AUTH_063_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPLqdtyStrssTstgRsltRpt"]
		@property
		def CCPLqdtyStrssTstgRsltRpt(self):
			return self._CCPLqdtyStrssTstgRsltRpt

		@CCPLqdtyStrssTstgRsltRpt.setter
		def CCPLqdtyStrssTstgRsltRpt(self, value):
			self._CCPLqdtyStrssTstgRsltRpt = value if type(value) != base_types.auto else self.make_default("CCPLqdtyStrssTstgRsltRpt")

		@CCPLqdtyStrssTstgRsltRpt.deleter
		def CCPLqdtyStrssTstgRsltRpt(self):
			del self._CCPLqdtyStrssTstgRsltRpt
			self._CCPLqdtyStrssTstgRsltRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPLqdtyStrssTstgRsltRpt', type=CCPLiquidityStressTestingResultReportV01, min=1, max=1, mutex_group=None, array=False),
		))