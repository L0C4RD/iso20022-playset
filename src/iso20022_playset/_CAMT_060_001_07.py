# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountReportingRequestV07

class CAMT_060_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.060.001.07"
		_docname = "camt.060.001.07"

		__slots__ = ["_AcctRptgReq"]
		@property
		def AcctRptgReq(self):
			return self._AcctRptgReq

		@AcctRptgReq.setter
		def AcctRptgReq(self, value):
			self._AcctRptgReq = value if value is not None else base_types.UninitialisedField(self, 'AcctRptgReq', AccountReportingRequestV07, False)

		@AcctRptgReq.deleter
		def AcctRptgReq(self):
			del self._AcctRptgReq
			self._AcctRptgReq = base_types.UninitialisedField(self, 'AcctRptgReq', AccountReportingRequestV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctRptgReq', type=AccountReportingRequestV07, min=1, max=1, mutex_group=None, array=False),
		))