# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractRegistrationStatementRequestV04

class AUTH_023_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.023.001.04"
		_docname = "auth.023.001.04"

		__slots__ = ["_CtrctRegnStmtReq"]
		@property
		def CtrctRegnStmtReq(self):
			return self._CtrctRegnStmtReq

		@CtrctRegnStmtReq.setter
		def CtrctRegnStmtReq(self, value):
			self._CtrctRegnStmtReq = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegnStmtReq', ContractRegistrationStatementRequestV04, False)

		@CtrctRegnStmtReq.deleter
		def CtrctRegnStmtReq(self):
			del self._CtrctRegnStmtReq
			self._CtrctRegnStmtReq = base_types.UninitialisedField(self, 'CtrctRegnStmtReq', ContractRegistrationStatementRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnStmtReq', type=ContractRegistrationStatementRequestV04, min=1, max=1, mutex_group=None, array=False),
		))