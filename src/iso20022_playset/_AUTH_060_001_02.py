# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPDailyCashFlowsReportV02 import CCPDailyCashFlowsReportV02

class AUTH_060_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.060.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CCPDalyCshFlowsRpt"]
		@property
		def CCPDalyCshFlowsRpt(self):
			return self._CCPDalyCshFlowsRpt

		@CCPDalyCshFlowsRpt.setter
		def CCPDalyCshFlowsRpt(self, value):
			self._CCPDalyCshFlowsRpt = value if type(value) != base_types.auto else self.make_default("CCPDalyCshFlowsRpt")

		@CCPDalyCshFlowsRpt.deleter
		def CCPDalyCshFlowsRpt(self):
			del self._CCPDalyCshFlowsRpt
			self._CCPDalyCshFlowsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPDalyCshFlowsRpt', type=CCPDailyCashFlowsReportV02, min=1, max=1, mutex_group=None, array=False),
		))