# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountReportRequestV04

class ACMT_013_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.013.001.04"
		_docname = "acmt.013.001.04"

		__slots__ = ["_AcctRptReq"]
		@property
		def AcctRptReq(self):
			return self._AcctRptReq

		@AcctRptReq.setter
		def AcctRptReq(self, value):
			self._AcctRptReq = value if value is not None else base_types.UninitialisedField(self, 'AcctRptReq', AccountReportRequestV04, False)

		@AcctRptReq.deleter
		def AcctRptReq(self):
			del self._AcctRptReq
			self._AcctRptReq = base_types.UninitialisedField(self, 'AcctRptReq', AccountReportRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctRptReq', type=AccountReportRequestV04, min=1, max=1, mutex_group=None, array=False),
		))