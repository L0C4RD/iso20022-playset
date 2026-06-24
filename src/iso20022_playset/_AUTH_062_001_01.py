# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPLiquidityStressTestingDefinitionReportV01 import CCPLiquidityStressTestingDefinitionReportV01

class AUTH_062_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.062.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

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