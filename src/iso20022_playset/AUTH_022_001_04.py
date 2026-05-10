from . import base_types
import ContractRegistrationStatementV04

class AUTH_022_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CtrctRegnStmt"]
		@property
		def CtrctRegnStmt(self):
			return self._CtrctRegnStmt

		@CtrctRegnStmt.setter
		def CtrctRegnStmt(self, value):
			self._CtrctRegnStmt = value if type(value) != auto else self.make_default("CtrctRegnStmt")

		@CtrctRegnStmt.deleter
		def CtrctRegnStmt(self):
			del self._CtrctRegnStmt
			self._CtrctRegnStmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnStmt', type=ContractRegistrationStatementV04, min=1, max=1, mutex_group=None, array=False),
		))

