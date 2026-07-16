# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPLiquidityStressTestingDefinitionReportV01

class AUTH_062_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01"
		_docname = "auth.062.001.01"

		__slots__ = ["_CCPLqdtyStrssTstgDefRpt"]
		@property
		def CCPLqdtyStrssTstgDefRpt(self):
			return self._CCPLqdtyStrssTstgDefRpt

		@CCPLqdtyStrssTstgDefRpt.setter
		def CCPLqdtyStrssTstgDefRpt(self, value):
			self._CCPLqdtyStrssTstgDefRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPLqdtyStrssTstgDefRpt', CCPLiquidityStressTestingDefinitionReportV01, False)

		@CCPLqdtyStrssTstgDefRpt.deleter
		def CCPLqdtyStrssTstgDefRpt(self):
			del self._CCPLqdtyStrssTstgDefRpt
			self._CCPLqdtyStrssTstgDefRpt = base_types.UninitialisedField(self, 'CCPLqdtyStrssTstgDefRpt', CCPLiquidityStressTestingDefinitionReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPLqdtyStrssTstgDefRpt', type=CCPLiquidityStressTestingDefinitionReportV01, min=1, max=1, mutex_group=None, array=False),
		))