# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPPortfolioStressTestingResultReportV01 import CCPPortfolioStressTestingResultReportV01

class AUTH_058_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.058.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CCPPrtflStrssTstgRsltRpt"]
		@property
		def CCPPrtflStrssTstgRsltRpt(self):
			return self._CCPPrtflStrssTstgRsltRpt

		@CCPPrtflStrssTstgRsltRpt.setter
		def CCPPrtflStrssTstgRsltRpt(self, value):
			self._CCPPrtflStrssTstgRsltRpt = value if type(value) != base_types.auto else self.make_default("CCPPrtflStrssTstgRsltRpt")

		@CCPPrtflStrssTstgRsltRpt.deleter
		def CCPPrtflStrssTstgRsltRpt(self):
			del self._CCPPrtflStrssTstgRsltRpt
			self._CCPPrtflStrssTstgRsltRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPPrtflStrssTstgRsltRpt', type=CCPPortfolioStressTestingResultReportV01, min=1, max=1, mutex_group=None, array=False),
		))