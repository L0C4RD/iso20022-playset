# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractRegistrationStatementV04

class AUTH_022_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04"
		_docname = "auth.022.001.04"

		__slots__ = ["_CtrctRegnStmt"]
		@property
		def CtrctRegnStmt(self):
			return self._CtrctRegnStmt

		@CtrctRegnStmt.setter
		def CtrctRegnStmt(self, value):
			self._CtrctRegnStmt = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegnStmt', ContractRegistrationStatementV04, False)

		@CtrctRegnStmt.deleter
		def CtrctRegnStmt(self):
			del self._CtrctRegnStmt
			self._CtrctRegnStmt = base_types.UninitialisedField(self, 'CtrctRegnStmt', ContractRegistrationStatementV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnStmt', type=ContractRegistrationStatementV04, min=1, max=1, mutex_group=None, array=False),
		))