# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPDailyCashFlowsReportV02

class AUTH_060_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02"
		_docname = "auth.060.001.02"

		__slots__ = ["_CCPDalyCshFlowsRpt"]
		@property
		def CCPDalyCshFlowsRpt(self):
			return self._CCPDalyCshFlowsRpt

		@CCPDalyCshFlowsRpt.setter
		def CCPDalyCshFlowsRpt(self, value):
			self._CCPDalyCshFlowsRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPDalyCshFlowsRpt', CCPDailyCashFlowsReportV02, False)

		@CCPDalyCshFlowsRpt.deleter
		def CCPDalyCshFlowsRpt(self):
			del self._CCPDalyCshFlowsRpt
			self._CCPDalyCshFlowsRpt = base_types.UninitialisedField(self, 'CCPDalyCshFlowsRpt', CCPDailyCashFlowsReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPDalyCshFlowsRpt', type=CCPDailyCashFlowsReportV02, min=1, max=1, mutex_group=None, array=False),
		))