# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContractRegistrationStatementV04 import ContractRegistrationStatementV04

class AUTH_022_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_CtrctRegnStmt"]
		@property
		def CtrctRegnStmt(self):
			return self._CtrctRegnStmt

		@CtrctRegnStmt.setter
		def CtrctRegnStmt(self, value):
			self._CtrctRegnStmt = value if type(value) != base_types.auto else self.make_default("CtrctRegnStmt")

		@CtrctRegnStmt.deleter
		def CtrctRegnStmt(self):
			del self._CtrctRegnStmt
			self._CtrctRegnStmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnStmt', type=ContractRegistrationStatementV04, min=1, max=1, mutex_group=None, array=False),
		))