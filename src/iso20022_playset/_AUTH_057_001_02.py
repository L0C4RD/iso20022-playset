# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPPortfolioStressTestingDefinitionReportV02 import CCPPortfolioStressTestingDefinitionReportV02

class AUTH_057_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.057.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

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