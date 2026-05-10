import base_types
import ContractRegistrationStatementRequestV04

class AUTH_023_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CtrctRegnStmtReq"]
		@property
		def CtrctRegnStmtReq(self):
			return self._CtrctRegnStmtReq

		@CtrctRegnStmtReq.setter
		def CtrctRegnStmtReq(self, value):
			self._CtrctRegnStmtReq = value if type(value) != auto else self.make_default("CtrctRegnStmtReq")

		@CtrctRegnStmtReq.deleter
		def CtrctRegnStmtReq(self):
			del self._CtrctRegnStmtReq
			self._CtrctRegnStmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnStmtReq', type=ContractRegistrationStatementRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

