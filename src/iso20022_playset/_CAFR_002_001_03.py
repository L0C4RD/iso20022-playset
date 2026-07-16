# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FraudReportingResponseV03

class CAFR_002_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cafr.002.001.03"
		_docname = "cafr.002.001.03"

		__slots__ = ["_FrdRptgRspn"]
		@property
		def FrdRptgRspn(self):
			return self._FrdRptgRspn

		@FrdRptgRspn.setter
		def FrdRptgRspn(self, value):
			self._FrdRptgRspn = value if value is not None else base_types.UninitialisedField(self, 'FrdRptgRspn', FraudReportingResponseV03, False)

		@FrdRptgRspn.deleter
		def FrdRptgRspn(self):
			del self._FrdRptgRspn
			self._FrdRptgRspn = base_types.UninitialisedField(self, 'FrdRptgRspn', FraudReportingResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdRptgRspn', type=FraudReportingResponseV03, min=1, max=1, mutex_group=None, array=False),
		))