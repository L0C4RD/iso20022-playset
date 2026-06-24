# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContractRegistrationStatementRequestV04 import ContractRegistrationStatementRequestV04

class AUTH_023_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.023.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CtrctRegnStmtReq"]
		@property
		def CtrctRegnStmtReq(self):
			return self._CtrctRegnStmtReq

		@CtrctRegnStmtReq.setter
		def CtrctRegnStmtReq(self, value):
			self._CtrctRegnStmtReq = value if type(value) != base_types.auto else self.make_default("CtrctRegnStmtReq")

		@CtrctRegnStmtReq.deleter
		def CtrctRegnStmtReq(self):
			del self._CtrctRegnStmtReq
			self._CtrctRegnStmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnStmtReq', type=ContractRegistrationStatementRequestV04, min=1, max=1, mutex_group=None, array=False),
		))