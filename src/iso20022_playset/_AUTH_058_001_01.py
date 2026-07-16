# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPPortfolioStressTestingResultReportV01

class AUTH_058_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01"
		_docname = "auth.058.001.01"

		__slots__ = ["_CCPPrtflStrssTstgRsltRpt"]
		@property
		def CCPPrtflStrssTstgRsltRpt(self):
			return self._CCPPrtflStrssTstgRsltRpt

		@CCPPrtflStrssTstgRsltRpt.setter
		def CCPPrtflStrssTstgRsltRpt(self, value):
			self._CCPPrtflStrssTstgRsltRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPPrtflStrssTstgRsltRpt', CCPPortfolioStressTestingResultReportV01, False)

		@CCPPrtflStrssTstgRsltRpt.deleter
		def CCPPrtflStrssTstgRsltRpt(self):
			del self._CCPPrtflStrssTstgRsltRpt
			self._CCPPrtflStrssTstgRsltRpt = base_types.UninitialisedField(self, 'CCPPrtflStrssTstgRsltRpt', CCPPortfolioStressTestingResultReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPPrtflStrssTstgRsltRpt', type=CCPPortfolioStressTestingResultReportV01, min=1, max=1, mutex_group=None, array=False),
		))